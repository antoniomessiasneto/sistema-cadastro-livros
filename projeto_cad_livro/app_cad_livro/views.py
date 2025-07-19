from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Livro, Autor, Genero
from django.db.models.functions import Lower
from django.db.models import Count 

def busca_ou_salva_autor(autor_nome: str):
    autor = Autor.objects.filter(nome__iexact=autor_nome).first()
    if not autor:
        autor = Autor.objects.create(nome=autor_nome)
    return autor

def busca_ou_salva_genero(genero_nome: str):
    genero = Genero.objects.filter(nome__iexact=genero_nome).first()
    if not genero:
        genero = Genero.objects.create(nome=genero_nome)
    return genero

def home(request):
    if request.method == 'GET':
        exibir = Livro.objects.all()
        autores_unicos = Livro.objects.values('autor').distinct().count()
        generos_unicos = Livro.objects.values('genero').distinct().count()
        return render(request, 'Usuario/home.html', {
            'exibir': exibir,
            'autores_unicos': autores_unicos,
            'generos_unicos': generos_unicos,
        })

    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        nome_autor = request.POST.get('autor')
        ano_publicacao = request.POST.get('ano_publicacao')
        nome_genero = request.POST.get('genero')
        quantidade_estoque = request.POST.get('quantidade_estoque')

        objeto_autor = busca_ou_salva_autor(nome_autor)
        objeto_genero = busca_ou_salva_genero(nome_genero)

        livro = Livro(
            titulo=titulo,
            autor=objeto_autor,
            ano_publicacao=ano_publicacao,
            genero=objeto_genero,
            quantidade_estoque=quantidade_estoque,
        )
        
        livro.save()
        return redirect('home')

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('home')

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        nome_autor = request.POST.get('autor')
        ano_publicacao = request.POST.get('ano_publicacao')
        nome_genero = request.POST.get('genero')
        quantidade_estoque = request.POST.get('quantidade_estoque')

        objeto_autor = busca_ou_salva_autor(nome_autor)
        objeto_genero = busca_ou_salva_genero(nome_genero)

        livro.titulo = titulo
        livro.autor = objeto_autor
        livro.ano_publicacao = ano_publicacao
        livro.genero = objeto_genero
        livro.quantidade_estoque = quantidade_estoque

        livro.save()
        return redirect('home')

