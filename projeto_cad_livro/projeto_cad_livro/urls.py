from django.urls import path
from app_cad_livro import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deletar_livro/<int:id>', views.deletar_livro, name="deletar_livro"),
    path('atualizar_livro/<int:id>', views.atualizar_livro, name="atualizar_livro"),
]