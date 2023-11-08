from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User


class Client(models.Model):

    PROVINCES = [
    ('Gauteng', 'Gauteng'),
    ('Free State', 'Free State'),
    ('Limpopo', 'Limpopo'),
    ]

    #Basic Fields
    client_name = models.CharField(null=True, blank=True, max_length=200)
    address_line_1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postal_code = models.CharField(null=True, blank=True, max_length=10)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    email_address = models.EmailField(null=True, blank=True, max_length=100)


    #Utility fields
    unique_id = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.client_name} {self.province} {self.unique_id}'


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split('-')[4]
            self.slug = slugify(f'{self.client_name} {self.province} {self.unique_id}')

        self.slug = slugify(f'{self.client_name} {self.province} {self.unique_id}')
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)