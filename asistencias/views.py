from django.shortcuts import render, redirect, get_object_or_404
from .models import Asistencia


# CREAR
def crear(request):

    if request.method == "POST":

        Asistencia.objects.create(
            tipo_documento=request.POST["tipo_documento"],
            documento=request.POST["documento"],
            nombres=request.POST["nombres"],
            apellidos=request.POST["apellidos"],
            whatsapp=request.POST["whatsapp"],
            fecha=request.POST["fecha"],
            asistio="asistio" in request.POST
        )

        return redirect("/asistencias/lista/")

    return render(request, "asistencias/formulario.html")


# LISTAR
def listar(request):

    asistencias = Asistencia.objects.all().order_by("-fecha", "apellidos")

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )


# VER
def detalle(request, id):

    asistencia = get_object_or_404(Asistencia, id=id)

    return render(
        request,
        "asistencias/detalle.html",
        {"asistencia": asistencia}
    )


# EDITAR
def editar(request, id):

    asistencia = get_object_or_404(Asistencia, id=id)

    if request.method == "POST":

        asistencia.tipo_documento = request.POST["tipo_documento"]
        asistencia.documento = request.POST["documento"]
        asistencia.nombres = request.POST["nombres"]
        asistencia.apellidos = request.POST["apellidos"]
        asistencia.whatsapp = request.POST["whatsapp"]
        asistencia.fecha = request.POST["fecha"]
        asistencia.asistio = "asistio" in request.POST

        asistencia.save()

        return redirect(f"/asistencias/detalle/{asistencia.id}/")

    return render(
        request,
        "asistencias/formulario.html",
        {"asistencia": asistencia}
    )


# ELIMINAR
def eliminar(request, id):

    asistencia = get_object_or_404(Asistencia, id=id)

    if request.method == "POST":
        asistencia.delete()
        return redirect("/asistencias/lista/")

    return render(
        request,
        "asistencias/confirmar_eliminar.html",
        {"asistencia": asistencia}
    )