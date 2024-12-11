from django.shortcuts import render, redirect
from django.views import View



class HomePage(View):

	def get(self, request):
		return render(request, "core/index.html")
