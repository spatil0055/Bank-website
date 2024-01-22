require('dotenv').config(); // Load environment variables from .env file

const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const { google } = require('google-auth-library');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files
app.use(express.static('public'));

// OAuth2 credentials
const credentials = {
    client_id: process.env.CLIENT_ID,
    client_secret: process.env.CLIENT_SECRET,
    redirect_uris: [process.env.REDIRECT_URI]
};
const oAuth2Client = new google.auth.OAuth2(credentials.client_id, credentials.client_secret, credentials.redirect_uris[0]);

// Get authorization URL
const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/gmail.send']
});

// Redirect to Gmail authorization URL
app.get('/auth', (req, res) => {
    res.redirect(authUrl);
});

// Handle the callback after Gmail has authorized the user
app.get('/auth/callback', async (req, res) => {
    const code = req.query.code;
    const { tokens } = await oAuth2Client.getToken(code);
    oAuth2Client.setCredentials(tokens);
    res.send('Authentication successful. You can now close this window.');
});

// Route to handle form submissions
app.post('/submit-form', async (req, res) => {
    const { name, clientemail, message } = req.body;

    try {
        const transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                type: 'OAuth2',
                user: process.env.EMAIL,
                clientId: process.env.CLIENT_ID,
                clientSecret: process.env.CLIENT_SECRET,
                refreshToken: oAuth2Client.credentials.refresh_token,
                accessToken: oAuth2Client.credentials.access_token,
            }
        });

        const mailOptions = {
            from: mail,
            to: process.env.WEBSITE_MAIL,
            subject: 'New Contact Form Submission',
            text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
        };

        await transporter.sendMail(mailOptions);
        res.status(200).send('OK');
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
