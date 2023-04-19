from django.db import models
import uuid

class Contact(models.Model):
    nama = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    pesan = models.TextField()
    def __str__(self):
        return self.nama
    
class order(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length= 30)
    email = models.EmailField(max_length = 30)
    alamat = models.CharField(max_length= 100)
    nohp = models.CharField(max_length= 30)
    pesanan = models.CharField(max_length= 50)
    def __str__(self):
        return self.nama
    