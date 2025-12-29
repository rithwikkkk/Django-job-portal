from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            # ROLE BASED REDIRECT
            if user.profile.role == "recruiter":
                return redirect("create_job")
            else:
                return redirect("job_list")

    return render(request, "accounts/login.html")
