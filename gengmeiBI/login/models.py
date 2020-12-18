from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    department = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'



