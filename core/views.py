from django.shortcuts import render, redirect
from django.views import View
from admin_app.models import (
	HeaderSlider, Book, Blog, Event
)



class HomePage(View):

	def get(self, request):
		context = {
			"sliders": HeaderSlider.objects.all().order_by("-id")[:2],
			"top_picks": Book.objects.all().order_by("-id")[:5],
		}
		return render(request, "core/index.html", context)
