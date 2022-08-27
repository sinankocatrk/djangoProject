from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Nick(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 17,verbose_name = "Server ")
    """content = models.CharField(max_length = 20,verbose_name = "Nick ") """
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title
