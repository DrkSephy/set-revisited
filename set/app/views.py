from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app.forms import UserForm
from django.contrib.auth import authenticate, login
from app.models import Product, Vendor

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

def shopping(request):
	items = Product.objects.all()
	return render(request, 'app/shopping.html', {'items': items})

def checkout(request):
	# TODO:
	# 	Send back array of quantities via POST request.
	#   The array index of each value will denote the item from the database
	#   i.e: index 0 will correspond to item 0 with pk=0, pk=1, etc

	if request.method == 'POST':
		quantities = request.POST.getlist('quantity')
		print quantities
	return render(request, 'app/checkout.html', {'things': quantities})

def bank(request):
	# TODO:
	#   Pass vendor information into form
	#   Form will have vendor section
	#     - Callback URL to check account
	#     - Summary of transaction
	#   Bank form will have the usual details for user
	#     - Card Name / Type
	#     - Card Number
	#     - Security Code
	#     - Address 
	#   Show Summary of transaction to take place
	#     - Items that are being bought
	#     - Quantities of each item
	#     - Description of each item
	#     - Total price of items
	
	# The callback will be a page that displays the vendor attributes
	# in order to check whether transactions went through
	data = {}
	data['callback'] = '/set/callback/'
	data['price'] = 9.99
	if request.method == 'POST':
		print 'Need to serve the bank form'
	return render(request, 'app/bank.html', {'vendor': data})