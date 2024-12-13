from django.db import models
from django.utils import timezone



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
