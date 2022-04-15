from django.shortcuts import render


def index(request):
    context = {
        "page_title": "DASHBOARD"
    }
    return render(request, 'dashboard/dashboard/index.html', context)


def charts(request):
    return render(request, 'dashboard/dashboard/charts.html')


def widgets(request):
    return render(request, 'dashboard/dashboard/widgets.html')


def tables(request):
    return render(request, "dashboard/dashboard/labo_pat_list.html")


def grid(request):
    return render(request, "dashboard/dashboard/grid.html")


def form_basic(request):
    return render(request, "dashboard/dashboard/form_basic.html")


def form_wizard(request):
    return render(request, "dashboard/dashboard/form_wizard.html")


def buttons(request):
    return render(request, "dashboard/dashboard/buttons.html")


def icon_material(request):
    return render(request, "dashboard/dashboard/icon-material.html")


def icon_fontawesome(request):
    return render(request, "dashboard/dashboard/icon-fontawesome.html")


def elements(request):
    return render(request, "dashboard/dashboard/elements.html")


def gallery(request):
    return render(request, "dashboard/dashboard/gallery.html")


def invoice(request):
    return render(request, "dashboard/dashboard/invoice.html")


def chat(request):
    return render(request, "dashboard/dashboard/chat.html")


