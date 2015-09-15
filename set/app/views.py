from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app.forms import UserForm
from django.contrib.auth import authenticate, login
from app.models import Product, Vendor, UserAccount
from decimal import *

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

# Route to display all items available to be purchased
def shopping(request):
	items = Product.objects.all()
	return render(request, 'app/shopping.html', {'items': items})

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
	#     - Quantities of each items
	#     - Description of each item
	#     - Total price of items
	
	# The callback will be a page that displays the vendor attributes
	# in order to check whether transactions went through
	summary = {}
	if request.method == 'POST':
		quantities = request.POST.getlist('quantity')
		summary['items'] = []
		for value in quantities: 
			if value != 0:
				itemDetails = {}
				item = Product.objects.all()[quantities.index(value)]
				itemDetails['name'] = item.name
				price = float(item.price) * float(value)
				itemDetails['price'] =  "%.2f" % price
				itemDetails['quantity'] = value
				summary['items'].append(itemDetails)
	total = 0.0
	for item in summary['items']:
		total += float(item['price'])

	summary['total'] = "%.2f" % total

	print summary

	return render(request, 'app/bank.html', {'vendor': summary})

def transaction(request):
	if request.method == 'POST':
		vendorName = request.POST.get('vendor name')
		userName = request.POST.get('name')
		total = request.POST.get('total price')
	vendor = Vendor.objects.get(name=vendorName)
	user = UserAccount.objects.get(name=userName)

	if float(user.account) >= float(total):
		print 'Yeah'
		user.account = Decimal(user.account) - Decimal(total)
		print user.account
		user.save()
		vendor.account += Decimal(total)
		print vendor.account
		vendor.save()


	return HttpResponse('Display summary of transaction')