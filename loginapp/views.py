from django.shortcuts import render
from .models import User
import mysql.connector
from operator import itemgetter

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def login(request):
        con = mysql.connector.connect(host="localhost",user="root",passwd="jigu2103",database="mysqldrc")
        cursor = con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",passwd="jigu2103",database="mysqldrc")
        cursor2 = con2.cursor()
        sqlcommand = "select email from loginappuser"
        sqlcommand2 = "select password from loginappuser"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        email=[]
        password=[]  
        for i in cursor:
            email.append(i)
        for j in cursor2:
            password.append(j)
        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))    
        con3 = mysql.connector.connect(host="localhost",user="root",password="jigu2103",database="mysqldrc")
        cursor3 = con2.cursor()

        if request.method =="POST":
            email = request.POST['email']
            password = request.POST['password']
            k=len(res)
            i=1
            sqlcommand3 = "select username from the loginapp where email = email"
            cursor3.execute(sqlcommand3)
            lst =[]
            for name in cursor3:
                name = name
                name2 =''.join(name)
            print(name2)
            while i <k:
                if res[i]==email and res2[i]==password:
                    return render(request,'welcome.html',{'name':name2})
                   break
                i+=1
            else:
             
                messages.info(request,"Check UserName or Password")
                return redirect('login')

    return render(request,'login.html')   
    return render(request,'welcome.html')
    
def register(request):
    if request.method =="POST":
        user = User()
        user.email = request.POST('email')
        user.username = request.POST('username')
        user.password = request.POST('password')
        user.repassword = request.POST('repassword')
        user.mobilenumber = request.POST('mobilenumber')
        if user.password!=user.repassword:
                messages.info(request,"Passwords not match")
                return redirect('register')
        elif user.fname=="" or user.lname=="" or user.email=="" or 
            user.password =="" or user.repassword=="":
                messages.info(request,"Some fields are missing")
                return redirect('register')   
        else:
            messages.info(request,"registration is sucessfully completed")
            user.save()

        return render(request,'register.html')
    else:
        return render(request,'register.html')   
            
    return render(request,'register.html')   
    
    