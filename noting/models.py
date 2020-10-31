from django.db import models
from django.contrib.auth.models import User

class notepad(models.Model):
    author = models.ForeignKey(User,related_name="note_author",on_delete=models.CASCADE)
    note_title=models.CharField(max_length=100,verbose_name="put a title")
    slug = models.SlugField(max_length=100,unique=True)
    note_content=models.TextField(verbose_name="write down your important note")
    note_image=models.ImageField(upload_to='note_image',verbose_name="Image")
    saving_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_title
# Create your models here.
