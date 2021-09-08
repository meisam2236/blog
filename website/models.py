from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension!')

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=True, blank=True, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=True, blank=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover', null=True, blank=True, validators=[validate_file_extension])
    content = RichTextField()
    createdDate = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    def __str__(self):
        return self.title