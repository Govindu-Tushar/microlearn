

from django.shortcuts import render
from .models import Course
def home(request):
    return render(request, 'marketplace/index.html')


def marketplace_page(request):
    courses = Course.objects.all()

    return render(
        request,
        "marketplace/marketplace.html",
        {"courses": courses}
    )
def student_dashboard(request):
    return render(request, 'marketplace/student_dashboard.html')

def instructor_dashboard(request):
    return render(request, 'marketplace/instructor_dashboard.html')



