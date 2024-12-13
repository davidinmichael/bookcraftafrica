from django.contrib import admin
from .models import (
	HeaderSlider, Book, Blog, Event
)


admin.site.register([HeaderSlider, Book, Blog, Event])
