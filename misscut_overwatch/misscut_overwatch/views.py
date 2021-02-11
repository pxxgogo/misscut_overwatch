from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def checking_view(request):
    if "username" in request.POST:
        return render(request, "checking.html", {"username": request.POST['username']})
    else:
        return HttpResponseRedirect("/")


def upload_template_view(request):
    return render(request, "upload_template.html")


def login_view(request):
    return render(request, "login.html")
