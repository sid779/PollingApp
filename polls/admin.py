from django.contrib import admin
from .models import Hackers

admin.site.site_header = 'PollsApp_AdminPanel'
admin.site.site_title = 'Polls AdminPanel'
admin.site.index_title = 'Welcome to pollsApp'

# Register your models here.
admin.site.register(Hackers)