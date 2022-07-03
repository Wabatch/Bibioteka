from django.contrib import admin

from book.models import Book
from users.models import Users

# Register your models here.

admin.site.register(Book)
admin.site.register(Users)

