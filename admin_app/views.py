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


class HeaderSliderView(View):

	def post(self, request):
		form = HeaderSliderForm(request.POST, request.FILES)
		if form.is_valid():
			header = form.save()
			return redirect("add_items")
		return redirect("home")


class BookView(View):

	def post(self, request):
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save()
			print("Book Saved")
			return redirect("add_items")
		print("Book not saved")
		print(form.errors)
		return redirect("home")


class BlogView(View):

	def post(self, request):
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			blog = form.save()
			return redirect("add_items")
		return redirect("home")


class EventView(View):

	def post(self, request):
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			event = form.save()
			return redirect("add_items")
		return redirect("home")