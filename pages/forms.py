# -*- coding: utf-8 -*-
from django import forms
from .fields import ReCaptchaField


class ReCaptchaForm(forms.Form):
    subject = forms.CharField(
            widget=forms.TextInput(
                    attrs={'class': 'validate[required] text-input'}))
    email = forms.EmailField(
            required=False,
            widget=forms.TextInput(attrs={'class': 'validate[required,custom[email]] text-input'}))
    message = forms.CharField(
            widget=forms.Textarea(attrs={
                'class': 'validate[required] text-input', 
                'rows': '8',
                'cols': '50'
                }))
    recaptcha = ReCaptchaField()
