from django.urls import path
from home.views import home_view, associacao_view, contato_view
from . import views

urlpatterns = [
    path('', home_view),
    path('associacao/', associacao_view),
    path("contato", contato_view)
]
