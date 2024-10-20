from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(
        request,
        "home/index.html"
    )

def associacao_view(request):
    return render(
        request,
        "associados/index.html"
    )

def contato_view(request):
    return render(
        request,
        "contato/index.html"
)