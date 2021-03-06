from django.db import models
from django.urls import reverse
from django.utils import timezone
from user.models import Profile


class Color(models.Model):
    name = models.CharField('Name', max_length=50, blank=True)
    number = models.CharField('Number', max_length=50, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    """Тип покупки"""

    name = models.CharField('Type of Purchase', max_length=100)
    slug = models.SlugField('Url', max_length=110)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = str(self.name.lower())
        super(Type, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('type_detail', kwargs={'type_slug': self.slug})





class Purchase(models.Model):
    """Покупки"""

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='Type', on_delete=models.CASCADE)
    cost = models.DecimalField('Cost $', decimal_places=2, max_digits=12)
    date = models.DateTimeField('Created Date', default=timezone.now())

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-date']

    def __str__(self):
        return str(self.type)

    def get_absolute_url(self):
        return reverse('purchase_detail', kwargs={'type_slug': self.type.slug, 'purchase_pk': self.pk})


