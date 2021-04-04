from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def register(request):
	if request.method == "POST":
		n=request.POST['uname']
		ct=request.POST['cn']
		add=request.POST['ad']
		e=request.POST['eml']
		a=request.POST['ag']
		d={'un':n,'con':ct,'as':add,'em':e,'age':a}
		return render (request,'html/details.html',{'hari':d})
	return render(request,'html/register.html')
