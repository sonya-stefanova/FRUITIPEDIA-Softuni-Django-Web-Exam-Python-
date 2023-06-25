from django.core.exceptions import ValidationError


def validate_first_letter_start(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_fruit_name_all_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")