from django.forms import ModelForm
from .models import Contact, order
from  django import forms

class FormContact(ModelForm) :
    class Meta:
        model = Contact
        exclude = ['id', 'tanggal']

        widgets = {
            'nama' : forms.TextInput({'class' : 'form-control'}),
            'email' : forms.TextInput({'class' : 'form-control'}),
            'pesan' : forms.TextInput({'class' : 'form-control'}),
        }

class formsOrder(ModelForm) :
    class Meta:
        model = order
        exclude = ['id']

        widgets = {
            'nama' : forms.TextInput({'class' : 'form-control'}),
            'email' : forms.TextInput({'class' : 'form-control'}),
            'alamat' : forms.TextInput({'class' : 'form-control'}),
            'nohp' : forms.TextInput({'class' : 'form-control'}),
            'pesanan' : forms.TextInput({'class' : 'form-control'}),
        }