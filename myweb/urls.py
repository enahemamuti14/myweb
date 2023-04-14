from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('send-contact/', views.send_contact, name='send_contact'),
    path('product/send-order/', views.send_order, name='send_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
