from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app.forms import UserForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
	return HttpResponse('Hello user!')

def userLogin(request):
	print 'hello user'

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()

	return render(request, 'app/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/set/')
			else:
				return HttpResponse('Your Set account is disabled')
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse('Invalid login credentials')
	else:
		return render(request, 'app/login.html', {})