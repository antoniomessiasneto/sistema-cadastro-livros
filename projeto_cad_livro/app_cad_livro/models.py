from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100)    
    def __str__(self):
        return self.nome

class Livro (models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    quantidade_estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

