from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Job, Application
from .forms import JobForm


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def create_job(request):
    if request.user.profile.role != 'recruiter':
        return HttpResponseForbidden("Only recruiters can post jobs")

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})


@login_required
def apply_job(request, job_id):
    if request.user.profile.role != 'seeker':
        return HttpResponseForbidden("Only job seekers can apply")

    job = get_object_or_404(Job, id=job_id)

    Application.objects.get_or_create(
        applicant=request.user,
        job=job
    )

    return redirect('job_list')


@login_required
def my_applications(request):
    if request.user.profile.role != 'seeker':
        return HttpResponseForbidden("Only job seekers can view applications")

    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'jobs/my_applications.html', {
        'applications': applications
    })
