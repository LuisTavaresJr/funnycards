from django.db import models



class Product(models.Model):

    title = models.CharField('titulo', max_length=100)
    photo = models.ImageField('foto')
    price = models.DecimalField('preço', decimal_places=2, max_digits=7)
    description = models.CharField('descrição', max_length=100)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.description