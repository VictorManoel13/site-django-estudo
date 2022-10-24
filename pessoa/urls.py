from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpadateView

urlpatterns = [
    path('', ListaPessoaView.as_view(), name = 'pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name = 'pessoa.novo'),
    path('editar/<int:pk>', PessoaUpadateView.as_view(), name = 'pessoa.editar'),
    
    
]
