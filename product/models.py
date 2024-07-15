# from django.conf import settings
from django.db import models
from django.conf import settings
from PIL import Image
import os


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


class Product(models.Model):
	name = models.CharField(max_length=255)
	short_descripion = models.TextField(max_length=255)
	long_description = models.TextField()
	image = models.ImageField(upload_to='pictures/%Y/%m', blank=True, null=True)
	slug = models.SlugField(unique=True)
	marketing_price = models.FloatField()
	promocional_marketing_price = models.FloatField(default=0)
	type_product = models.CharField(
		default='V',
		max_length=1,
		choices=(
				('V', 'Variação'),
				('S', 'Simples'),
			)
		)

	# Função de Redimensionamento de imagem.
	@staticmethod
	def resize_image(img, new_width=800):
		image_full_path = os.path.join(settings.MEDIA_ROOT, img.name)	# Pega caminho da imagem
		img_pil = Image.open(image_full_path)	# Usa o Pillow para abrir a imagem
		original_widht, original_height = img_pil.size

		if original_widht > new_width:
			new_height = round((new_width * original_height) / original_widht)	# Calcula altura da imagem, mantendo proporção
			new_image = img_pil.resize((new_width, new_height), Image.LANCZOS)	# Cria nova imagem, com nova largura e altura.
			new_image.save(		# Salva imagem no mesmo lugar que a anterior, porém com novas dimensões
					image_full_path,
					optimize = True,
					quality=90
				)

		img_pil.close()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		max_image_size = 800

		if self.image:
			self.resize_image(self.image, max_image_size)


	def __str__(self):
		return self.name

