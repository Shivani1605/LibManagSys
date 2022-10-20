


from django.contrib import admin
from django.urls import path,include
from book_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>/', views.student_api),
    path('auth/',include('rest_framework.urls'))
    
]
