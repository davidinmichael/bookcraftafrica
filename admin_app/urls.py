from django.urls import path
from .views import AddHeader

urlpatterns = [
	path("add-header/", AddHeader.as_view(), name="add-header"),
]
