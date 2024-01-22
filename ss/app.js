const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
const port = 3000; // You can change the port if needed

// Middleware to parse incoming request data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files (e.g., HTML, CSS, images)
app.use(express.static('public'));

// Route to handle form submissions
app.post('/submit-form', (req, res) => {
    const { name, email, message } = req.body;

    // Create a transporter with your email credentials
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: mail, // Replace with your email
            pass: 'P@til@1234' // Replace with your password or use an app password
        }
    });

    // Set up the email options
    const mailOptions = {
        from: email,
        to: 'sproox.s.s@example.com', // Replace with your website mail
        subject: 'New Contact Form Submission',
        text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
    };

    // Send the email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.status(500).send('Internal Server Error');
        } else {
            console.log('Email sent: ' + info.response);
            res.status(200).send('OK');
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
