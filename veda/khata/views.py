from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,AccountSerializer,DepositeSerializer,LoanSerializer,HeroImageSerializer
from rest_framework import status
import jwt,datetime
from .models import User,openaccount,depositetype,applyloan,heroImages
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_UNAUTHORIZED)

class LoginView(APIView):
  def post(self, request):
    
    email = request.data['email']
    password = request.data['password']
    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('User not Found')

    
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password')

    response = Response()
    

        
        
    response.set_cookie(key='jwt', value=token, httponly=True)
    # # localStorage.setItem('token', token)
    response.data = {'token': token}
    return response
  
# class UserView(APIView):
#     def get(self, request):
        
       
     

#         # Check if the Authorization header is present
#         if 'Authorization' in request.headers:
#             auth_header = request.headers['Authorization']
#             # Split the header to extract the token
#             token = auth_header.split(' ')[1]
      

        

#         if not token:
#             raise AuthenticationFailed('Unauthenticated')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])

#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated')

#         user = User.objects.filter(id=payload['id']).first()

#         if not user:
#             raise AuthenticationFailed('User not found')

#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request):
        
        token = request.COOKIES.get('jwt')
       
        print(token)
        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
           
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            "message":"You are log out"
        }
        return response
    
class openbankaccount(APIView):
    def post(self,request):
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class deposite(APIView):
    def post(self,request):
        serializer=DepositeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ApplyLoan(APIView):
    def post(self,request):
        serializer=LoanSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class newbankaccdetail(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(token)  # Print the token for debugging

        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            print("User not found")
            raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
        account_data = openaccount.objects.all()
        # user = User.objects.filter(id=payload['id']).first()

        if account_data is None:
            print("Account data not found for the user")
            raise AuthenticationFailed('Unauthenticated')

        # Serialize the account data using the openaccountSerializer
        serializer = AccountSerializer(account_data,many=True)

        return Response(serializer.data)

class newdeposite(APIView):
   
    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(token)  # Print the token for debugging

        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            print("User not found")
            raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
        account_data =depositetype.objects.all()
        # user = User.objects.filter(id=payload['id']).first()

        if account_data is None:
            print("Account data not found for the user")
            raise AuthenticationFailed('Unauthenticated')

        serializer=DepositeSerializer(account_data,many=True)

        return Response(serializer.data)
    

class LendLoan(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(token)  # Print the token for debugging

        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            print("User not found")
            raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
        account_data =applyloan.objects.all()
        # user = User.objects.filter(id=payload['id']).first()

        if account_data is None:
            print("Account data not found for the user")
            raise AuthenticationFailed('Unauthenticated')

        serializer=LoanSerializer(account_data,many=True)

        return Response(serializer.data)


class heroimg(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        print(token)  # Print the token for debugging

        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            print("User not found")
            raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
        account_data =heroImages.objects.all()
        # user = User.objects.filter(id=payload['id']).first()

        if account_data is None:
            print("Account data not found for the user")
            raise AuthenticationFailed('Unauthenticated')

        serializer=HeroImageSerializer(account_data,many=True)

        return Response(serializer.data)
    

class uploadimg(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        print(token)  # Print the token for debugging

        if not token:
            print("dint get token")
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            print("User not found")
            raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
        account_data =heroImages.objects.all()
        # user = User.objects.filter(id=payload['id']).first()

        if account_data is None:
            print("Account data not found for the user")
            raise AuthenticationFailed('Unauthenticated')
        serializer=HeroImageSerializer(instance=account_data,data=request.data)
        if serializer.is_valid():
            account_data.save()
        return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def uploadimg(request):
    token = request.COOKIES.get('jwt')
    print(token)  # Print the token for debugging

    if not token:
        print("Didn't get a token")
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

    except jwt.ExpiredSignatureError:
        print("Token has expired")
        raise AuthenticationFailed('Unauthenticated')

    user = User.objects.filter(id=payload['id']).first()
    if user is None:
        print("User not found")
        raise AuthenticationFailed('Unauthenticated')

    # Create a new instance of the heroImages model
    new_image = heroImages()


    # Set the image field with the request data
    new_image.image = request.data.get('image')

    # Save the new image record
    new_image.save()

    return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def deleteimg(request,pk):
    token = request.COOKIES.get('jwt')
    print(token)  # Print the token for debugging

    if not token:
        print("dint get token")
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(f"Decoded Payload: {payload}")  # Print the decoded payload for debugging

    except jwt.ExpiredSignatureError:
        print("Token has expired")
        raise AuthenticationFailed('Unauthenticated')

    user = User.objects.filter(id=payload['id']).first()
    if user is None:
        print("User not found")
        raise AuthenticationFailed('Unauthenticated')

        # Query the openaccount model to retrieve user's account data
    account_data =heroImages.objects.get(id=pk)
        # user = User.objects.filter(id=payload['id']).first()

    account_data.delete()
    return Response({'message': 'Image Deleted successfully'}, status=status.HTTP_201_CREATED)
    
                        