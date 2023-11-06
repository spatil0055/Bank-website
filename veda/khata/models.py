from datetime import *
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import usermanager
class User(AbstractUser):
    USER_TYPE=(
        ('admin','Admin'),
        ('customer','Customer'),
    )
     
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    profile = models.ImageField(upload_to='media/images/',default='default_image.jpg')
    user_type=models.CharField(max_length=20,choices=USER_TYPE, default='customer')
    
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=usermanager()

class openaccount(models.Model):
    ACCOUNT_TYPE=[
        ('SAVING ACCOUNT','saving account'),
        ('CORPORATE SALARY ACCOUNT','corporate salary account'),
        ('SENIOR CITIZEN SAVING ACCOUNT','senior citizen saving account'),
        ('CURRENT ACCOUNT','current account'),
        ('NRI SAVING ACCOUNT','nri saving account')

    ]
    OCCUPATION_LIST=[
        ('DOCTOR','doctor'),
        ('ENGINEER','engineer'),
        ('BUSINESSMAN','businessman'),
        ('CHARTERED ACCOUNTANT','chartered accountant'),
        ('STUDENT','student')

    ]

    INCOME_SOURCE=[
        ('SALARY','salary'),
        ('BUSINESS','business'),
        ('STOCKS','stocks'),
        ('POCKET MONEY','pocket money'),
        ('RENT','rent')
    ]
    email=models.EmailField(max_length=255,default='')
    accountType=models.CharField(max_length=100,default='',choices=ACCOUNT_TYPE)
    phone=models.CharField(max_length=20,default='')
    pan=models.CharField(max_length=20,default='')
    aadhar=models.CharField(max_length=20,default='')
    occupation=models.CharField(max_length=255,choices=OCCUPATION_LIST,default='')
    incomeSource=models.CharField(max_length=20,choices=INCOME_SOURCE,default='')
    grossAnnualIncome=models.CharField(max_length=20,default='')
    selected=models.BooleanField(default=False)
    
    def __str__(self):
        return self.email


class depositetype(models.Model):
    DEPOSITE_TYPE=[
        ("FIXED DEPOSIT","fixed deposit"),
        ('RECURRING DEPOSIT','recurring deposit'),
        ('NRI FIXED DEPOSIT','nri fixed deposit'),
        ('SAFE DEPOSIT LOCKER','safee deposit locker')
    ]

    CITY=[
        ('AGRA','agra'),
        ('AHMEDABAD','ahmedabad'),
        ('AJMER','ajmer'),
        ('ANAND','anand'),
        ('ANKLESHWAR','ankleshwar'),
        ('BANGALORE','banglore'),
        ('BELGAUM','belgum'),
        ('BHILWARA','bhilwara'),
        ('BHOPAL','bhopal'),
        ('BIAORA','biaora'),
        ('BURHANPUR','burhanpur'),
        ('CHANDIGARH','chandigarh'),
        ('CHENNAI','chennai'),
        ('CHITTORGARH','chittorgarh'),
        ('COIMBATORE','coimbatore'),
        ('DAVANGERE','davangere'),
        ('DEHRADUN','dehradun'),
        ('DELHI NCR','delhi ncr'),
        ('DHAR','dhar'),
        ('DHARWAD','dharwad'),
        ('ERODE','erode'),
        ('GOKAK','gokak'),
        ('GUNTUR','guntur'),
        ('HARDA','harda'),
        ('HARVERI','harveri'),
        ('HIMMATNAGER','himmatnager'),
        ('HUBLI','hubli'),
        ('HYDERABAD','hyderabad'),
        ('INDORE','indore'),
        ('JAIPUR','jaipur'),
        ('JALANDHAR','jalandhar'),
        ('JAMKHANDI','jamkhandi'),
        ('JODHPUR','jodhpur'),
        ('KAKINADA','kakinada'),
        ('KANPUR','kanpur'),
        ('KHANDWA','khandwa'),
        ('KHARGAONE','khargaone'),
        ('KOCHI','kochi'),
        ('KOLKATA','kolkata'),
        ('KOTA','kota'),
        ('LUCKNOW','lucknow'),
        ('LUDHIANA','ludhiana'),
        ('MADURAI MANDSAUR','madurai mandsaur'),
        ('MORBI','morbi'),
        ('MUMBAI','mumbai'),
        ('NAGPUR','nagpur'),
        ('NASHIK','nashik'),
        ('NEEMUCH','neemuch'),
        ('PANIPAT','panipat'),
        ('PATAN','patan'),
        ('PIPARIYA','pipariya'),
        ('PUNE','pune'),
        ('RAIPUR','raipur'),
        ('RAJAHMUNDRY','rajamundry'),
        ('RAJGARH','rajgarh'),
        ('RAJKOT','rajkot'),
        ('RATLAM','ratlam'),
        ('SALEM','salem'),
        ('SANAWAD','sanawad'),
        ('SURAT','surat'),
        ('TANUKU','tanuku'),
        ('TIRUPPUR','tiruppur'),
        ('UJJAIN','ujjain'),
        ('VADODARA','vadodata'),
        ('VAPI','vapi'),
        ('VIJAYWADA','vijaywada'),
        ('VIZAG','vizag')
    ]

    product=models.CharField(max_length=20,default='',choices=DEPOSITE_TYPE)
    city=models.CharField(max_length=20,default='',choices=CITY)
    fullname=models.CharField(max_length=100,default='')
    email=models.EmailField(max_length=255,default='')
    phone=models.CharField(max_length=20,default='')
    selected=models.BooleanField(default=False)

    def __str__(self):
        return self.email

class applyloan(models.Model):
    LOAN_TYPE=[
        ('PERSONAL LOAN','personal loan'),
        ('HOME LOAN','home loan'),
        ('EDUCATION LOAN','education loan'),
        ('CAR LOAN','car loan'),
        ('TWO WHEELER LOAN','two wheeler loan'),
        ('GOLD LOAN','gold loan'),
        ('PROPERTY LOAN','property loan')

    ]
    name=models.CharField(max_length=255,default='')
    email=models.EmailField(max_length=255,default='')
    address=models.CharField(max_length=255,default='')
    # dob=models.DateField(default=timezone.now,null=False,blank=False)
    pan=models.CharField(max_length=20,default='')
    aadhar=models.CharField(max_length=20,default='')
    amount=models.CharField(max_length=20,default='')
    tenure=models.CharField(max_length=3,default='')
    loanType=models.CharField(max_length=20,default='',choices=LOAN_TYPE)
    selected=models.BooleanField(default=False)

    def __str__(self):
        return self.aadhar

class heroImages(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    image = models.ImageField(upload_to='media/images/', default='default_image.jpg')
    def __str__(self):
        return str(self.id)





