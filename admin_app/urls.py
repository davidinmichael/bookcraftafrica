from django.urls import path
from .views import (
	AddPlatformItems
)

urlpatterns = [
	path("add-items/", AddPlatformItems.as_view(), name="add-items"),
]
