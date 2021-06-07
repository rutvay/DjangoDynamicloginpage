from django.shortcuts import render
from .models import user
from django.shortcuts import redirect
from django.contrib import messages
from . import urls
from operator import itemgetter
import mysql.connector
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
data = user()
fetcher = user()
mydb = mysql.connector.connect(host="localhost", user="root", password="rutvaydhami", database="RUTVAY")
mycursor = mydb.cursor()
# user for signup page
dummy = user()
sqlform = "Insert into login values(%s,%s,%s,%s)"

def base(request):
    return render(request, 'home.html')



def login(request):
    if request.method == 'POST':
        # google = request.POST.get('name')
        # print(google)
        fetcher.email = request.POST['email']
        fetcher.password = request.POST['password']
        query = "Select * from login WHERE email=%s"
        val = [(str(fetcher.email))]
        mycursor.execute(query, val)
        result = mycursor.fetchall()
        for res in result:
            if fetcher.email in res:
                if fetcher.password == res[3]:
                    dummy.fname = res[0]
                    return redirect('/home')
                else:
                    messages.info(request,"Wrong Password")
                    errormess = {'mess' : "Oh no! Wrong password try again" }
                    return render(request, 'loggin.html', {'error':errormess})
        errormess = {'mess': "User not found please signup"}
        return render(request, 'loggin.html', {'error': errormess})
    return render(request, 'loggin.html')

def home(request):
    datadict = {'fname': dummy.fname }
    return render(request, 'home.html',{'data': datadict})

def signup(request):
    if request.method == 'POST':
        data.email = request.POST['email']
        data.password = request.POST['password']
        data.fname = request.POST['fname']
        data.lname = request.POST['lname']
        #Finds this email into the data base first
        query = "Select * from login WHERE email=%s"
        val = [(str(data.email))]
        mycursor.execute(query, val)
        result = mycursor.fetchall()
        for res in result:
            if data.email in res:
                error = {'mess':"This email already exsist please login" }
                return render(request, 'siggnup.html', {'errormess':error})
        vals = [[data.fname,data.lname,data.email,data.password]]
        mycursor.executemany(sqlform,vals)
        mydb.commit()
        data.save()
        return redirect('/login')
    return render(request, 'siggnup.html')