from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key =settings.STRIPE_SECRET_KEY
# Create your models here.
class profiles(models.Model):
	name = models.CharField(max_length=150)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	description = models.TextField(default='decription default text')

	# location = models.CharField(max_length=150, default='location default')
	# job = models.CharField(max_length=150, null=True)
	def __str__(self):
		return self.name

class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username


def stripeCallback(sender, request, user, **kwargs):
	user_stripe_account, created = userStripe.objects.get_or_create(user=user)
	if created:
		print ('created for %s'%(user.username))
	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_account.stripe_id = new_stripe_id['id']
		user_stripe_account.save()

def profilesCallback(sender, request, user, **kwargs):
	userProfiles, is_created = profiles.objects.get_or_create(user=user)
	if is_created:
		userProfiles.name = user.username
		userProfiles.save()


user_logged_in.connect(stripeCallback)
user_signed_up.connect(stripeCallback)
user_signed_up.connect(profilesCallback)
