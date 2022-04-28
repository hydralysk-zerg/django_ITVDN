from datetime import timedelta
from re import T
from unicodedata import decimal
from django.db import models

from django.contrib.auth.models import User

class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True)
    description = models.TextField(null=True)
    delivered_at = models.DateTimeField(auto_created=True, blank=True)
    could_use_in_bouquet = models.BooleanField(default=True)
    wiki_page = models.URLField(default='https://www.wikipedia.org/', name=
        'Wikipedia', unique_for_date='delivered_at')
    name = models.CharField(max_length=64, unique=True)


class Bouquet(models.Model):
    frech_period = models.DurationField(default=timedelta(days=5), help_text=
        'Use this field wen you need to have information about bouquet fresh time')
    photo = models.ImageField(blank=True)
    price = models.FloatField(default=1.0)
    flowers = models.ManyToManyField(Flower, verbose_name=
        'This bouquet constants of this flowers')

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_email = models.EmailField()
    diname = models.CharField(max_length=64)
    invoice = models.FileField()
    user_uuid = models.UUIDField(auto_created=True, editable=False)
    discount_size = models.DecimalField(decimal_places=5, max_digits=5, blank=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')

