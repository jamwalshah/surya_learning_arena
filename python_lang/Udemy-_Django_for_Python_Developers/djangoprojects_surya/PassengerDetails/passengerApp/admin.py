from django.contrib import admin
from passengerApp.models import PassengerPatal

# Register your models here.
class PassengerAdminPatal(admin.ModelAdmin):
    # restricting the fields to expose into admin console (not showing email field)
    list_display = ['firstName', 'lastName', 'rewardPoints']

# registering the model with Model Admin class to be displayed in admin console

admin.site.register(model_or_iterable=PassengerPatal, admin_class=PassengerAdminPatal)
