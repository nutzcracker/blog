from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Dossier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	photo = models.ImageField(upload_to='media', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	tag = TaggableManager()
	url = models.SlugField(null=True)



	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Объект'
		verbose_name = 'Объект'
		ordering = ['name']

class Comment(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()



    def __str__(self):
        return self.text
