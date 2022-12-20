from django.db import models

# Create your models here.


class bathsulmasail(models.Model):
    nama = models.CharField(max_length=150)
    deskripsi = models.TextField(default = 'ok')
    
     

   
        
