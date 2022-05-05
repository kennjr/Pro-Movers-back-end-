from django.contrib import admin

# Register your models here.
from backendapp.models import User


class UserAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('email', 'username', )
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('username', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(User, UserAdmin)