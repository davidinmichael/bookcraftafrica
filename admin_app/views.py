from django.shortcuts import render, redirect
from django.views import View

from .models import (
	HeaderSlider, Book, Blog, Event
)

from .forms import (
	HeaderSliderForm, BookForm, BlogForm, EventForm
)


class AddPlatformItems(View):
	def get(self, request):
		return render(request, "admin_app/add-items.html")


class HeaderSliderView(Views):

	def post(self, request):
		form = HeaderSliderForm(request.POST, request.FILES)
		if form.is_valid():
			header = form.save()
			return redirect("add-items")
		return redirect("home")


class BookView(Views):

	def post(self, request):
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save()
			return redirect("add-items")
		return redirect("home")