from django.contrib import admin
from django.urls import path
from tweet import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.get,name='get'),
    path("",views.home),
    path('predict', views.predict, name = 'make predictions')

]
