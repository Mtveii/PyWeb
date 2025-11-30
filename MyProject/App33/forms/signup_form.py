# Інструментарій Django для роботи з формами
from django import forms
from django.core.exceptions import ValidationError
import re   # regular expressions

# класи-форми описують склад форм у вигляді спеціальних елементів
class SignupForm(forms.Form) :
    first_name = forms.CharField(
        min_length=2, 
        max_length=64, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести ім'я",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 64 символи"
        })
    
    last_name  = forms.CharField(
        min_length=2, 
        max_length=64, 
        label="Прізвище",
        error_messages={
            'required': "Необхідно ввести прізвище",
            'min_length': "Прізвище повинно мати щонайменше 2 символи",
            'max_length': "Прізвище не повинно перевищувати 64 символи"
        })
        
    phone  = forms.CharField(
        min_length=10, 
        max_length=13,   # +38 098 765 43 21
        label="Телефон",
        error_messages={
            'required': "Необхідно ввести Телефон",
            'min_length': "Телефон повинен мати щонайменше 10 символів",
            'max_length': "Телефон не повинен перевищувати 13 символів"
        })
        
    email = forms.CharField(
        min_length=6, 
        max_length=128, 
        label="E-mail",
        error_messages={
            'required': "Необхідно ввести E-mail",
            'min_length': "E-mail повинен мати щонайменше 6 символів",
            'max_length': "E-mail не повинен перевищувати 128 символів"
        })

    birthdate = forms.DateField(
        required=False,
        label="Дата народження"
    )

    login = forms.CharField(
        min_length=3, 
        max_length=32, 
        label="Логін",
        error_messages={
            'required': "Необхідно ввести Логін",
            'min_length': "Логін повинен мати щонайменше 3 символи",
            'max_length': "Логін не повинен перевищувати 32 символи"
        })

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': "Необхідно ввести пароль"
        }
    )

    repeat = forms.CharField(                         # повтор паролю
        widget=forms.PasswordInput(), 
        required=False )
    
    is_agree = forms.BooleanField(
        help_text="Я приймаю політику конфіденційності сайту",
        error_messages={
            'required': "Ви маєте погодитись з політикою конфіденційності сайту"
        }
    )


    def clean(self):                                  # Custom validation
        cleaned_data = super().clean()                # базова валідація
        if 'password' in cleaned_data :               # Умова на те, що пароль пройшов базову валідацію
            password = cleaned_data['password']       # Беремо за основу значення, що пройшло перевірку
            if len(password) < 4 :                    # та додаємо наступну групу перевірок
                self.add_error(                       # Реєструємо нову помилку валідації
                    "password",                       #  для поля "password"
                    ValidationError("Пароль має містити принаймні 4 символи"))
            if not re.search(r"\d", password) :       # умова від зворотнього - не знайдено цифру
                   self.add_error(                    # без elif - обидві помилки можуть
                    "password",                       # бути одночасно
                    ValidationError("Пароль має містити принаймні одну цифру"))
                   
        if 'repeat' in cleaned_data :        
            repeat = cleaned_data['repeat']
            if repeat != cleaned_data.get('password', '') :
                self.add_error(
                    'repeat',
                    ValidationError("Повтор не збігається з паролем")
                )

        if 'first_name' in cleaned_data :        
            first_name = cleaned_data['first_name']   # використання регулярного виразу-шаблону 
            if re.search(r"\d", first_name):          # для пошуку в імені довільної цифри
                self.add_error('first_name',
                    ValidationError("В імені не допускаються цифри"))
                
        return cleaned_data
            
'''
Д.З. Забезпечити розширену валідацію форми користувача
телефон
е-пошта
логін -- не повинен містити ":"
дата народження (якщо є, то має бути у минулому, * обмежити мін. вік)
'''