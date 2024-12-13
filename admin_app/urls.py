from django.urls import path
from .views import (
	AddPlatformItems, HeaderSliderView, BookView,
	BlogView, EventView
)

urlpatterns = [
	path("add-items/", AddPlatformItems.as_view(), name="add_items"),
	path("add-header/", HeaderSliderView.as_view(), name="add_header"),
	path("add-book/", BookView.as_view(), name="add_book"),
	path("add-blog/", BlogView.as_view(), name="add_blog"),
	path("add-event/", EventView.as_view(), name="add_event"),
]
