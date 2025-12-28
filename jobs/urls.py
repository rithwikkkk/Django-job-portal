from django.urls import path
from .views import job_list, create_job, apply_job
from .views import my_applications

urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', create_job, name='create_job'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('my-applications/',my_applications,name='my_applications'),
]

