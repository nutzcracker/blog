from django.db import models

# Create your models here.
class Dossier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	photo = models.ImageField(upload_to='media', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Объект'
		verbose_name = 'Объект'
		ordering = ['name']
