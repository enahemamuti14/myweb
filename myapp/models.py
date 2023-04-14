from django.db import models

class Contact(models.Model):
    nama = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    pesan = models.TextField()
    tanggal = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nama
    
class order(models.Model):
    nama = models.CharField(max_length= 30)
    email = models.EmailField(max_length = 30)
    alamat = models.CharField(max_length= 100)
    nohp = models.CharField(max_length= 30)
    pesanan = models.CharField(max_length= 50)
    def __str__(self):
        return self.nama
    