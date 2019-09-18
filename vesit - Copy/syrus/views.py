from django.shortcuts import render

def home(request):
	return render(request,'syrus/home.html')
def login(request):
	return render(request,'syrus/login.html')
def register(request):
	return render(request,'syrus/register.html')
def about(request):
	return render(request,'syrus/about.html')
def help(request):
	return render(request,'syrus/help.html')
def Missions(request):
	return render(request,'syrus/Missions.html')
def Resources(request):
	return render(request,'syrus/Resources.html') 