from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.marketplace_page, name='marketplace'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor-dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('payment/', views.payment, name="payment"),
    path('acknowledgment/', views.acknowledgment, name='acknowledgment'),
    path('qr/', views.qr_page, name='qr_page'),
]

