from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from fruitipedia_app.web.validators import validate_first_letter_start, validate_fruit_name_all_letters


# Create your models here.
class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1
    MAX_LEN_EMAIL = 40
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8
    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators = (MinLengthValidator(MIN_LEN_FIRST_NAME),
                      validate_first_letter_start,
                      ),
        null = False,
        blank = False,
        verbose_name = 'First Name',
    )

    last_name = models.CharField(
        max_length = MAX_LEN_LAST_NAME,
        validators = (MinLengthValidator(MIN_LEN_LAST_NAME),
                      validate_first_letter_start,
                      ),
        null=False,
        blank=False,
        verbose_name = 'Last Name',

    )
    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators = (MinLengthValidator(MIN_LEN_PASSWORD),),
        null=False,
        blank=False,
    )

    #----optional fields------:

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name = "Image URL",
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default = DEFAULT_AGE,
    )


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Fruit(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators = (MinLengthValidator(MIN_LEN_NAME), validate_fruit_name_all_letters,),
        verbose_name = 'Fruit Name',
        null = False,
        blank = False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name = 'Fruit Image URL'
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name  = 'Fruit Description',
    )

    #----optional field------:

    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name = 'Nutrition Info',
    )

    def __str__(self):
        return f'{self.name}'