# Інструментарій Django для роботи з формами
from django import forms

# класи-форми описують склад форм у вигляді спеціальних елементів
class DemoForm(forms.Form) :
    first_name = forms.CharField(min_length=2, max_length=64, label="Ім'я")
    last_name  = forms.CharField(min_length=2, max_length=64, label="Прізвище")
