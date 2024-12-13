from django import forms
from .models import (
	HeaderSlider, Book, Blog, Event
)


class HeaderSliderForm(forms.ModelForm):

	class Meta:
		model = HeaderSlider
		fields = "__all__"


class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = "__all__"


class BlogForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = "__all__"


class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = "__all__"