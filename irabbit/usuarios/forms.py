# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserModelForm(forms.ModelForm):

    User._meta.get_field('first_name').blank = False
    User._meta.get_field('email').blank = False
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255, 'placeholder': "Login", }),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255, 'placeholder': "Nome"}),
            'email': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255, 'placeholder': "Email"}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'maxlength': 255, 'placeholder': "Senha"})
        }

        error_messages = {
            'username': {"required": 'O campo Login é obrigatório'},
            'first_name': {"required": 'O campo Nome é obrigatório'},
            'email': {"required": 'O campo Email é obrigatório'},
            'password': {"required": 'O campo Senha é obrigatório'}
        }


        # def clean_password2(self):
        #     password1 = self.cleaned_data.get("password1")
        #     password2 = self.cleaned_data.get("password2")
        #     if password1 and password2 and password1 != password2:
        #         raise forms.ValidationError(
        #             self.error_messages['password_mismatch'],
        #             code='password_mismatch',
        #         )
        #     return password2

    # def clean(self):
    #     self.cleaned_data = super().clean()
    #
    #     if not self.cleaned_data.get('first_name') and not self.cleaned_data.get('phone'):
    #         print('nao valido ssdfsd')
    #         raise ValidationError('Informe o seu email ou telefone')
    #     print('galoooo')
    #     return self.cleaned_data

    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
             user.save()
        return user

