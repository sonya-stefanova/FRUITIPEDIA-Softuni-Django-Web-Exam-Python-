from django import forms
from fruitipedia_app.web.models import Profile, Fruit


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            ),

        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            ),

        }

class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age',)


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description','nutrition')



class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),

            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),

        }
class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')


        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }

class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('nutrition',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
