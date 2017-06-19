from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key =settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY

	#get user stripe id from user model
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		# Get the payment token submitted by the form:
		token = request.POST['stripeToken']

		#to save customer card details when making a charge
		customer = stripe.Customer.retrieve(customer_id)
		customer.sources.create(source=token)
		# customer = stripe.Customer.retrieve({CUSTOMER_ID})
		# customer.sources.create(source={TOKEN_ID})
		
		# Charge the user's card:
		charge = stripe.Charge.create(
			amount=1000,
			currency="gbp",
			description="Example charge",
			customer=customer,
			# source=token,
			)		
	context = {'publishKey':publishKey}
	template = 'checkout.html'
	return render(request, template, context)

