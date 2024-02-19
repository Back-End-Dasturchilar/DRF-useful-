from django.contrib import admin

from contact.models import Contact, ContactInfo

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactInfo)