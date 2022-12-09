from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import Author

admin.site.register(Author)