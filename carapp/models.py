from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Profile(models.Model):

    SELLER = [
        ('Dealer', 'Dealer'),
        ('Osoba Prywatna', 'Osoba Prywatna'),
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location_city = models.CharField(max_length=50, null=True, blank=False)
    location_country = models.CharField(max_length=50, null=True, blank=False)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    seller = models.CharField(max_length=200, null=True, blank=False, choices=SELLER)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default='profiles/user.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Advert(models.Model):

    YES_OR_NO = [
        ('Tak', 'Tak'),
        ('Nie', 'Nie'),
    ]

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(9999999), MinValueValidator(1000)])
    variant = models.CharField(max_length=200, null=True, blank=False)
    brand = models.ForeignKey('Brand', null=True, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=50, null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    description = models.TextField(max_length=3500, null=True, blank=False)
    featured_image1 = models.ImageField(null=True, blank=True)
    featured_image2 = models.ImageField(null=True, blank=True)
    featured_image3 = models.ImageField(null=True, blank=True)
    fuel_type = models.ForeignKey('Fuel', null=True, on_delete=models.DO_NOTHING)
    engine_capacity = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(9999), MinValueValidator(300)])
    power = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(5000), MinValueValidator(40)])
    mileage = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(500000), MinValueValidator(100)])
    no_crashed = models.CharField(max_length=200, null=True, blank=False, choices=YES_OR_NO)
    first_registration = models.DateField(null=True, blank=False)
    color = models.CharField(max_length=200, null=True, blank=False)
    num_of_doors = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(10), MinValueValidator(1)])
    color_type = models.CharField(max_length=200, null=True, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single-advert', kwargs={'id': str(self.id)})

    @property
    def get_photo_url(self):
        if self.featured_image1 and hasattr(self.featured_image1, 'url'):
            return self.featured_image1.url
        else:
            return "/static/images/bmwcs.jpg"


class Brand(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class PriceReminderConnection(models.Model):
    user_address = models.EmailField(max_length=200)
    id_of_advert = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.user_address
