from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class BookCategory(models.TextChoices):
	FICTION = "fiction", _("Fiction")
	NON_FICTION = "non_fiction", _("Non Fiction")
	ADVENTURE = "adventure", _("Adventure")
	KIDS = "kids", _("Kids")
	TECHNOLOGY = "technology", _("Technology")
	OTHERS = "others", _("Others")


class BaseModel(models.Model):
	date_added = models.DateField(default=timezone.now, null=True, blank=True)
	updated_at = models.DateField(auto_now=True, null=True, blank=True)

	class Meta:
		abstract = True


class HeaderSlider(BaseModel):
	title = models.CharField(max_length=50, null=True, blank=True)
	subtitle = models.CharField(max_length=50, null=True, blank=True)
	button_one = models.CharField(max_length=15, null=True, blank=True)
	button_two = models.CharField(max_length=15, null=True, blank=True)
	banner_img = models.ImageField(upload_to="banner_img/")

	def __str__(self):
		return f"{self.title} | {self.subtitle}"


class Book(BaseModel):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50, null=True, blank=True)
	description = models.TextField()
	category = models.CharField(max_length=50, null=True, blank=True, choices=BookCategory.choices, default=BookCategory.OTHERS)
	pages = models.CharField(max_length=10, null=True, blank=True)
	year_published = models.CharField(max_length=5, null=True, blank=True)
	book_type = models.CharField(max_length=20, null=True, blank=True)
	book_cover = models.ImageField(upload_to="book_cover/")
	snippet = models.TextField(null=True, blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.title)
			self.slug = f"{base_slug}-{self.id}"

		if not self.snippet:
			self.snippet = ' '.join(self.description.split()[:20])
		return super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.title} | {self.author}"


class Blog(BaseModel):
	title = models.CharField(max_length=100)
	blog_body = models.TextField()
	blog_img = models.ImageField(upload_to="blog_img/", null=True, blank=True)
	snippet = models.TextField(null=True, blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.title)
			self.slug = f"{base_slug}-{self.id}"

		if not self.snippet:
			self.snippet = ' '.join(self.description.split()[:20])
		return super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.title}"


class Event(BaseModel):
	title = models.CharField(max_length=100)
	description = models.TextField()
	event_date = models.DateField(null=True, blank=True)
	event_time = models.TimeField(null=True, blank=True)
	event_img = models.ImageField(upload_to="event_img/", null=True, blank=True)

	def __str__(self):
		return f"{self.title}"

