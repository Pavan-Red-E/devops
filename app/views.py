from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from django.http import HttpResponse

def home(request):
	return render(request, 'index.html',{})
def register(request):
	request.session.flush()
	return render(request, 'Login.html',{})
def login(request):
	return render(request, 'Reg.html',{})

def analyticspage(request):
	return render(request, 'Analytics.html',{})
def resu(request):
	return render(request, 'resu.html',{})
def contactpage(request):
	return render(request, 'Contact.html',{})
@csrf_exempt
def saveuser(request):
	if request.method=="POST":
		text=' '
		n=request.POST.get('name')
		g=request.POST.get('gender')
		ph=request.POST.get('phone')
		p=request.POST.get('password')
		e=request.POST.get('email')
		ob=UserData.objects.all()
		d=0
		for elt in ob:
			if e==elt.email:
				text='User already Signed In'
				d=1
				break
		if d==0:
			obj=UserData(name=n,password=p,email=e,gender=g,phone=ph)
			obj.save()
			text='Account Created Successfully'
		context={'text':text}
		return render(request,'regresult.html',context)
@csrf_exempt
def checklogin(request):
	text=" "
	d=0
	e=request.POST.get('email')
	p=request.POST.get('password')
	obj=UserData.objects.all()
	name=''
	for elt in obj:
		if e==elt.email and p==elt.password:
			d=1
			name=elt.name
			request.session['email'] = e
			request.session['name'] = elt.name
			break
	if d==0:
		con={'text':"No User Found"}
		return render(request,"regresult.html",con)
	else:
		return render(request,'index.html',{'name':name})
