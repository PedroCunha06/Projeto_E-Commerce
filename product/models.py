from django.db import models

'''
Produto:
        Produto:
            nome - Char
            descricao_curta - Text
            descricao_longa - Text
            imagem - Image
            slug - Slug
            preco_marketing - Float
            preco_marketing_promocional - Float
            tipo - Choices
                ('V', 'Variável'),
                ('S', 'Simples'),

        Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
'''

class Produto(models.Model):
	nome = models.CharField(max_length=255)
	descricao_curta = models.TextField(max_length=255)
	descricao_longa = models.TextField()
	imagem = models.ImageField(upload_to='pictures/%Y/%m', blank=True, null=True)
	slug = models.SlugField(unique=True)
	preco_marketing = models.FloatField()
	preco_marketing_promocional = models.FloatField(default=0)
	tipo = models.CharField(
		default='V',
		max_length=1,
		choices=(
				('V', 'Variação'),
				('S', 'Simples'),
			)
		)
