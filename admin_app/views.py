from django.shortcuts import render, redirect
from django.views import View


class AddPlatformItems(View):
	def get(self, request):
		return render(request, "admin_app/add-header.html")