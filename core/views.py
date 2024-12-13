from django.shortcuts import render, redirect
from django.views import View
from admin_app.models import (
	HeaderSlider, Book, Blog, Event
)



class HomePage(View):

	def get(self, request):
		books = Book.objects.all().order_by("-id")
		context = {
			"sliders": HeaderSlider.objects.all().order_by("-id")[:2],
			"top_picks": books[:5],
			"books": books[:6],
			"blogs": Blog.objects.all().order_by("-id")[:10],
			"events": Event.objects.all().order_by("-id")[:4],
		}
		return render(request, "core/index.html", context)
