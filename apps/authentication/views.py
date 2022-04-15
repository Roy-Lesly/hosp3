from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, SignUpForm
from apps.accounts.models import Account


def login_view(request):
    if request.method == 'GET':
        cache.set('next', request.GET.get('next', None))
    template = "authentication/authentication-login.html"
    form = LoginForm(request.POST or None)
    form2 = SignUpForm()
    msg = ""
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                check_user = Account.objects.get(username=username)
                if check_user.check_password(password):
                    user = authenticate(request, username=username, password=password)
                    test = str(check_user)
                    login(request, user)
                    if cache.get("next"):
                        return redirect(cache.get("next"))
                    if test == "zane" or test == "admin":
                        print("Logged as Admin/Zane")
                        return redirect("/root")
                    elif test == "Laboratory":
                        print("Logged as Laboratory")
                        return redirect("/labo")
                    elif test == "Radiology":
                        print("Logged as Radiology")
                        return redirect("/radi")
                    elif test == "Registration":
                        print("Logged as Registration")
                        return redirect("/regi")
                    elif test == "Maternity":
                        print("Logged as Maternity")
                        return redirect("/mate")
                    elif test == "Ward":
                        print("Logged as Ward")
                        return redirect("/ward")
                    elif test == "Pharmacy":
                        print("Logged as Pharmacy")
                        return redirect("/phar")
                    elif test == "Orthopedics":
                        print("Logged as Orthopedics")
                        return redirect("/orth")
                    elif test == "TSD":
                        return redirect("/tsd")
                    else:
                        print("Not Logged In")
                else:
                    print("pwd Not ok")
                    msg = 'Invalid Password'
                    return render(request, template, {'msg': msg})
                    # return redirect("/")

            except Account.DoesNotExist:
                print("Department Invalid")
                msg = "Department Invalid"
                return render(request, template, {'msg': msg})

        else:
            msg = 'Error validating the form'
    context = {
        "form": form, "msg": msg, "form2": form2, "title": "LOGIN"}
    return render(request, template, context)


def register_user(request):
    print("here")
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        print(form.is_valid())
        print(form.errors)
        if password1 == password2:
            try:
                Account.objects.get(username__exact=request.POST['username'])
                msg = form.errors
                return JsonResponse({"data": msg}, safe=False)
            except Account.DoesNotExist:
                print("Does Not Exist")
                if form.is_valid():
                    form.save()
                    print("saved")
                    user = request.POST['username']

                    msg = 'Department created for ' + user
                    return JsonResponse({"data": msg}, safe=False)
                else:
                    msg = form.errors
                    return JsonResponse({"data": msg}, safe=False)
        else:
            # msg = "Passwords Donot Match"
            msg = form.errors
            return JsonResponse({"data": msg}, safe=False)
    else:
        form = SignUpForm()

    return render(request, "authentication/authentication-login.html", {"form": form, "msg": msg, "success": success})


