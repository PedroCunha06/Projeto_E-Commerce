# from django.conf import settings
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from PIL import Image
import os
from utils.format import format_price


class Product(models.Model):
	name = models.CharField(max_length=255)
	short_description = models.TextField(max_length=255)
	long_description = models.TextField()
	image = models.ImageField(upload_to='pictures/%Y/%m', blank=True, null=True)
	slug = models.SlugField(unique=True, blank=True, null=True)
	marketing_price = models.FloatField()
	promocional_marketing_price = models.FloatField(default=0)
	type_product = models.CharField(
		default='V',
		max_length=1,
		choices=(
				('V', 'Variable'),
				('S', 'Simple'),
			)
		)

	def formatted_marketing_price(self):
		return format_price(self.marketing_price)

	def formatted_promotional_price(self):
		return format_price(self.promocional_marketing_price)

	formatted_marketing_price.short_description = 'Price'
	formatted_promotional_price.short_description = 'Promotional Price'
 
 
	# Função de Redimensionamento de imagem.
	@staticmethod
	def resize_image(img, new_width=800):
		image_full_path = os.path.join(
		    settings.MEDIA_ROOT, img.name)  # Pega caminho da imagem
		img_pil = Image.open(image_full_path)  # Usa o Pillow para abrir a imagem
		original_widht, original_height = img_pil.size

		if original_widht > new_width:
			# Calcula altura da imagem, mantendo proporção
			new_height = round((new_width * original_height) / original_widht)
			# Cria nova imagem, com nova largura e altura.
			new_image = img_pil.resize((new_width, new_height), Image.LANCZOS)
			new_image.save(		# Salva imagem no mesmo lugar que a anterior, porém com novas dimensões
					image_full_path,
					optimize=True,
					quality=90
				)

		img_pil.close()

	def save(self, *args, **kwargs):
		if not self.slug:
			slug = f'{slugify(self.name)}'  # Cria um slug automaticamente
			self.slug = slug

		super().save(*args, **kwargs)

		max_image_size = 800

		if self.image:
			self.resize_image(self.image, max_image_size)

	def __str__(self):
		return self.name


class Variation(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)	# Modo cascata
	price = models.FloatField()
	promocional_price = models.FloatField(default=0)
	stock = models.PositiveIntegerField(default=1)


	def __str__(self):
		return self.name or self.product.name	# Mostra nome ou nome do produto ligado
