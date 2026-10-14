from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def iniciar_sesion(request):
    if request.method == "POST":
        usuario = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if usuario is not None:
            login(request, usuario)
            return redirect(request.GET.get("next", "/asistencias/lista/"))
        return render(request, "usuarios/login.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "usuarios/login.html")


def registro(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(request, "usuarios/registro.html", {"error": "Las contraseñas no coinciden"})
        if len(password1) < 8:
            return render(request, "usuarios/registro.html", {"error": "La contraseña debe tener mínimo 8 caracteres"})
        if User.objects.filter(username=username).exists():
            return render(request, "usuarios/registro.html", {"error": "Ese usuario ya existe"})

        usuario = User.objects.create_user(username=username, email=email, password=password1)
        login(request, usuario)
        return redirect("/asistencias/lista/")
    return render(request, "usuarios/registro.html")


def cerrar_sesion(request):
    logout(request)
    return redirect("/usuarios/login/")