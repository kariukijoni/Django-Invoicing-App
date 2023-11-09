from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User


class Client(models.Model):

    PROVINCES=[
    ('Gauteng', 'Gauteng'),
    ('Free State', 'Free State'),
    ('Limpopo', 'Limpopo'),
    ]

    #Basic Fields
    client_name=models.CharField(null=True, blank=True, max_length=200)
    address_line_1=models.CharField(null=True, blank=True, max_length=200)
    client_logo=models.ImageField(default='default_logo.png',upload_to='company_logos')
    province=models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postal_code=models.CharField(null=True, blank=True, max_length=10)
    phone_number=models.CharField(null=True, blank=True, max_length=100)
    email_address=models.EmailField(null=True, blank=True, max_length=100)
    tax_number = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    unique_id=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.client_name} {self.province} {self.unique_id}'


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created=timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id=str(uuid4()).split('-')[4]
            self.slug=slugify(f'{self.client_name} {self.province} {self.unique_id}')

        self.slug=slugify(f'{self.client_name} {self.province} {self.unique_id}')
        self.last_updated=timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)


class Invoice(models.Model):
    TERMS=[
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]

    STATUS=[
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title=models.CharField(null=True, blank=True, max_length=100)
    number=models.CharField(null=True, blank=True, max_length=100)
    due_date=models.DateField(null=True, blank=True)
    payment_terms=models.CharField(choices=TERMS, default='14 days', max_length=100)
    status=models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes=models.TextField(null=True, blank=True)

    #RELATED fields
    client_invoice=models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    unique_id=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.title} {self.unique_id}'


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created=timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id=str(uuid4()).split('-')[4]
            self.slug=slugify()

        self.slug=slugify(f'{self.title} {self.unique_id}')
        self.last_updated=timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


class Product(models.Model):
    CURRENCY=[
    ('R', 'ZAR'),
    ('$', 'USD'),
    ]

    title=models.CharField(null=True, blank=True, max_length=100)
    description=models.TextField(null=True, blank=True)
    quantity=models.FloatField(null=True, blank=True)
    price=models.FloatField(null=True, blank=True)
    currency=models.CharField(choices=CURRENCY, default='R', max_length=100)

    # Related fields
    product_invoice=models.ForeignKey(Invoice, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    unique_id=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.title} {self.unique_id}'


    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created=timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id=str(uuid4()).split('-')[4]
            self.slug=slugify(f'{self.title} {self.unique_id}')

        self.slug=slugify(f'{self.title} {self.unique_id}')
        self.last_updated=timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)



class Settings(models.Model):

    PROVINCES=[
    ('Gauteng', 'Gauteng'),
    ('Free State', 'Free State'),
    ('Limpopo', 'Limpopo'),
    ]

    #Basic Fields
    client_name=models.CharField(null=True, blank=True, max_length=200)
    client_logo=models.ImageField(default='default_logo.jpg', upload_to='company_logos')
    address_line_1=models.CharField(null=True, blank=True, max_length=200)
    province=models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postal_code=models.CharField(null=True, blank=True, max_length=10)
    phone_number=models.CharField(null=True, blank=True, max_length=100)
    email_address=models.CharField(null=True, blank=True, max_length=100)
    tax_number=models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    unique_id=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.client_name} {self.province} {self.unique_id}'


    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created=timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id=str(uuid4()).split('-')[4]
            self.slug=slugify(f'{self.client_name} {self.province} {self.unique_id}')

        self.slug=slugify(f'{self.client_name} {self.province} {self.unique_id}')
        self.last_updated=timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)

    class Meta:
        # db_table=''
        # managed=True
        # verbose_name='ModelName'
        verbose_name_plural='Settings'