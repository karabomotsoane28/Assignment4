from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),
    path('page',views.page, name="page"), 
    path('home',views.home, name="home"),
    path('',views.index, name="index"),
    path('show',views.show,  name="show"),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  