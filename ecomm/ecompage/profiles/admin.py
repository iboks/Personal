from django.contrib import admin

# Register your models here.
from .models import profiles, userStripe
class profilesAdmin(admin.ModelAdmin):
	class Meta:
		model = profiles

admin.site.register(profiles, profilesAdmin)

class userStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = userStripe

admin.site.register(userStripe, userStripeAdmin)