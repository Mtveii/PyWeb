# Інструментарій Django для роботи з формами
from django import forms
from django.core.exceptions import ValidationError
import re  


class form_user(forms.Form) :
    first_name = forms.CharField(
        min_length=2, 
        max_length=6, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести ім'я",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 64 символи"
        })
    
    last_name  = forms.CharField(
        min_length=2, 
        max_length=6, 
        label="Прізвище",
        error_messages={
            'required': "Необхідно ввести прізвище",
            'min_length': "Прізвище повинно мати щонайменше 2 символи",
            'max_length': "Прізвище не повинно перевищувати 64 символи"
        })

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': "Необхідно ввести пароль"
        }
    )
    phone = forms.CharField(
        min_length=10,
        max_length=10,
        label="Номер телефону",
        error_messages={
            'required': "Необхідно ввести номер телефону",
            'min_length': "Номер телефону повинен містити 10 цифр",
            'max_length': "Номер телефону повинен містити 10 цифр"
        }
    )


    def clean(self):                                  
        cleaned_data = super().clean()               
        if 'password' in cleaned_data :              
            password = cleaned_data['password']      
            if len(password) < 4 :                    
                self.add_error(                      
                    "password",                       
                    ValidationError("Пароль має містити принаймні 4 символи"))
            if not re.search(r"\d", password) :       
                   self.add_error(                   
                    "password",                       
                    ValidationError("Пароль має містити принаймні одну цифру"))

        if 'first_name' in cleaned_data :        
            first_name = cleaned_data['first_name']   
            if re.search(r"\d", first_name):          
                self.add_error('first_name',
                    ValidationError("В імені не допускаються цифри"))
        
        if 'phone' in cleaned_data:
            phone = cleaned_data['phone']
            if not re.fullmatch(r"\d+", str(phone)):
                self.add_error(
                    'phone',
                    ValidationError("Номер телефону може містити лише цифри")
                )
        return cleaned_data
            
