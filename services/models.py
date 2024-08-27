from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User

class Services(models.Model):
    title = models.CharField("عنوان", max_length=255)
    content = RichTextField("محتوا")
    status = models.BooleanField("وضعیت", default=False)
    created_date = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)
    updated_date = models.DateTimeField("تاریخ بروزرسانی", auto_now=True)
    image = models.ImageField("تصویر", upload_to='services_images/')     
    class Meta:
        ordering = ['-created_date']
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return "{}-{}".format(self.title, self.id)