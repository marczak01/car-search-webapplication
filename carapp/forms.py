from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm
from .models import User, Profile, Advert
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                                'class': 'bg-light form-control',
                                'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({
                                'id': 'password',
                                'class': 'form-control bg-light',
                                'placeholder': 'Enter your password'})


class CaptchaPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'bg-light form-control', 'placeholder': 'Enter your email'})


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                    'id': 'email',
                                    'class': 'bg-light form-control',
                                    'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'id': 'password',
                                    'class': 'bg-light form-control',
                                    'placeholder': 'Enter password'}))


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
                                'id': 'password1',
                                'class': 'bg-light form-control',
                                'placeholder': 'Wprowadź hasło'})
        self.fields['password2'].widget.attrs.update({
                                'id': 'password2',
                                'class': 'bg-light form-control',
                                'placeholder': 'Powtórz hasło'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                                    'id': 'username',
                                    'class': 'bg-light form-control',
                                    'placeholder': 'Wprowadź nazwę użytkownika'}),
            'email': forms.EmailInput(attrs={
                                    'id': 'email',
                                    'class': 'bg-light form-control',
                                    'placeholder': 'Wprowadź adres e-mail'}),
            # 'password1' : forms.PasswordInput(attrs={
            #                         'id': 'password1',
            #                         'class': 'form-control bg-light',
            #                         'placeholder': 'Enter password'}),
            # 'password2' : forms.PasswordInput(attrs={
            #                         'id': 'password2',
            #                         'class': 'form-control bg-light',
            #                         'placeholder': 'Repeat password'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'email', 'username', 'location_city', 'location_country', 'seller', 'phone_number',
                  'bio', 'profile_image']
        labels = {
            'name':   _('Full Name'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                                'id': 'name',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'surname': forms.TextInput(attrs={
                                'id': 'name',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'email': forms.TextInput(attrs={
                                'id': 'eMail',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'username': forms.TextInput(attrs={
                                'id': 'username',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'location_city': forms.TextInput(attrs={
                                'id': 'locationCity',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'location_country': forms.TextInput(attrs={
                                'id': 'locationCountry',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'seller': forms.Select(attrs={
                                'id': 'seller',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'phone_number': forms.TextInput(attrs={
                                'id': 'shortIntro',
                                'class': 'bg-light form-control',
                                'disabled': 'disabled'}),
            'bio': forms.Textarea(attrs={
                                'id': 'bio',
                                'class': 'bg-light form-control',
                                'rows': '7',
                                'maxlength': '300',
                                'minlength': '20',
                                'disabled': 'disabled'}),
            'profile_image': forms.FileInput(attrs={
                                'id': 'imageProfile',
                                'class': 'edit-photo rounded-circle img-fluid border border-dark',
                                'disabled': 'disabled'}),
        }


class ProfileFormEditable(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'email', 'username', 'location_city', 'location_country', 'seller', 'phone_number',
                  'bio', 'profile_image']
        labels = {
            'name':   _('Full Name'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                                'id': 'name',
                                'class': 'bg-light form-control'}),
            'surname': forms.TextInput(attrs={
                                'id': 'name',
                                'class': 'bg-light form-control'}),
            'email': forms.TextInput(attrs={
                                'id': 'eMail',
                                'class': 'bg-light form-control'}),
            'username': forms.TextInput(attrs={
                                'id': 'username',
                                'class': 'bg-light form-control'}),
            'location_city': forms.TextInput(attrs={
                                'id': 'locationCity',
                                'class': 'bg-light form-control'}),
            'location_country': forms.TextInput(attrs={
                                'id': 'locationCountry',
                                'class': 'bg-light form-control'}),
            'seller': forms.Select(attrs={
                                'id': 'seller',
                                'class': 'bg-light form-control'}),
            'phone_number': forms.TextInput(attrs={
                                'id': 'shortIntro',
                                'class': 'bg-light form-control'}),
            'bio': forms.Textarea(attrs={
                                'id': 'bio',
                                'class': 'bg-light form-control',
                                'rows': '7',
                                'maxlength': '300',
                                'minlength': '20'}),
            'profile_image': forms.FileInput(attrs={
                                'id': 'imageProfile'}),
        }


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'price', 'variant', 'brand',
                  'address', 'phone', 'description',
                  'featured_image1', 'featured_image2', 'featured_image3',
                  'fuel_type', 'engine_capacity',
                  'power', 'mileage', 'no_crashed',
                  'first_registration', 'color',
                  'num_of_doors', 'color_type', ]

        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'title', 'class': 'bg-light form-control', 'placeholder': 'Enter title'}),
            'price': forms.NumberInput(attrs={'id': 'price', 'class': 'bg-light form-control', 'placeholder': 'PLN'}),
            'variant': forms.TextInput(
                attrs={'id': 'variant', 'class': 'bg-light form-control', 'placeholder': 'Enter variant'}),
            'brand': forms.Select(attrs={'id': 'brand', 'class': 'bg-light form-control'}),
            'address': forms.TextInput(
                attrs={'id': 'address', 'class': 'bg-light form-control', 'placeholder': 'Enter your address'}),
            'phone': forms.TextInput(
                attrs={'id': 'phone', 'class': 'bg-light form-control', 'placeholder': 'Enter number phone',
                       'pattern': "[0-9]{3}-[0-9]{3}-[0-9]{3}"}),
            'description': forms.Textarea(
                attrs={'id': 'description', 'class': 'bg-light form-control', 'placeholder': 'Max 5000 character'}),
            'featured_image1': forms.FileInput(attrs={'id': 'featured_image1', 'class': 'form-control-file'}),
            'featured_image2': forms.FileInput(attrs={'id': 'featured_image2', 'class': 'form-control-file'}),
            'featured_image3': forms.FileInput(attrs={'id': 'featured_image3', 'class': 'form-control-file'}),
            'fuel_type': forms.Select(attrs={'id': 'fuel_type', 'class': 'bg-light form-control'}),
            'engine_capacity': forms.NumberInput(attrs={'id': 'engine_capacity', 'class': 'bg-light form-control'}),
            'power': forms.NumberInput(attrs={'id': 'power', 'class': 'bg-light form-control', 'placeholder': 'HP'}),
            'mileage': forms.NumberInput(attrs={'id': 'mileage', 'class': 'bg-light form-control'}),
            'no_crashed': forms.Select(attrs={'id': 'no_crashed', 'class': 'form-control'}),
            'first_registration': forms.DateInput(
                attrs={'id': 'first_registration', 'class': 'bg-light form-control'}),
            'color': forms.TextInput(attrs={'id': 'color', 'class': 'form-control'}),
            'num_of_doors': forms.NumberInput(attrs={'id': 'num_of_doors', 'class': 'form-control'}),
            'color_type': forms.TextInput(attrs={'id': 'color_type', 'class': 'form-control'}),
        }


class EmailPriceForm(forms.Form):

    name = forms.CharField(max_length=25)
    your_address = forms.EmailField()
    your_phone = forms.CharField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
                            'class': 'bg-light form-control',
                            'placeholder': 'Wprowadź swoje imie i nazwisko'})
        self.fields['name'].label = "Imię i Nazwisko:"
        self.fields['your_address'].widget.attrs.update({
                            'class': 'bg-light form-control',
                            'placeholder': 'Podaj swój adres e-mail'})
        self.fields['your_address'].label = "Twój e-mail:"
        self.fields['your_phone'].widget.attrs.update({
                            'class': 'bg-light form-control',
                            'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{3}',
                            'placeholder': 'Podaj swój numer telefonu np. 777-888-999'})
        self.fields['your_phone'].label = "Numer telefonu:"
        self.fields['comments'].widget.attrs.update({
                            'class': 'bg-light form-control',
                            'placeholder': 'Dodaj wiadomość do sprzedawcy (opcjonalne)'})
        self.fields['comments'].label = "Komentarz:"


class EmailPriceReminderForm(forms.Form):

    your_address = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['your_address'].widget.attrs.update({
                                'class': 'bg-light form-control',
                                'placeholder': 'Podaj swój adres e-mail'})
        self.fields['your_address'].label = "Twój e-mail:"
