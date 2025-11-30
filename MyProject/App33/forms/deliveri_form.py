from django import forms
from django.core.exceptions import ValidationError
import re   # regular expressions

# класи-форми описують склад форм у вигляді спеціальних елементів
class DeliveriForm(forms.Form) :
    first_name = forms.CharField(
        min_length=2, 
        max_length=20, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести first_name",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 20 символи"
        })
    
    last_name = forms.CharField(
        min_length=2, 
        max_length=20, 
        label="last_name",
        error_messages={
            'required': "Необхідно ввести last_name",
            'min_length': "last_name повинно мати щонайменше 2 символи",
            'max_length': "last_name не повинно перевищувати 20 символи"
        })
    
    Street_Address = forms.CharField(
        min_length=5, 
        max_length=50, 
        label="Street Address",
        error_messages={
            'required': "Необхідно ввести Street_Address",
            'min_length': "Street_Address повинно мати щонайменше 5 символи",
            'max_length': "Street_Address не повинно перевищувати 50 символи"
        })
    
    Street_Address_L2 = forms.CharField(
        min_length=5, 
        max_length=50, 
        label="Street Address Line 2",
        error_messages={
            'required': "Необхідно ввести Street_Address_L2",
            'min_length': "Street_Address_L2 повинно мати щонайменше 5 символи",
            'max_length': "Street_Address_L2 не повинно перевищувати 50 символи"
        })
    
    City = forms.CharField(
        min_length=2, 
        max_length=10, 
        label="City",
        error_messages={
            'required': "Необхідно ввести City",
            'min_length': "City повинно мати щонайменше 2 символи",
            'max_length': "City не повинно перевищувати 10 символи"
        })
    
    Region = forms.CharField(
        min_length=8, 
        max_length=15, 
        label="Region",
        error_messages={
            'required': "Необхідно ввести Region",
            'min_length': "Region повинно мати щонайменше 8 символи",
            'max_length': "Region не повинно перевищувати 15 символи"
        })
    
    index = forms.CharField(
        min_length=4, 
        max_length=6, 
        label="Postal / Zip Code",
        error_messages={
            'required': "Необхідно ввести Postal / Zip Code",
            'min_length': "Postal / Zip Code повинно мати щонайменше 4 символи",
            'max_length': "Postal / Zip Code повинно перевищувати 6 символи"
        })
                
    
    Romania = forms.CharField(
        label="Romania",
        error_messages={
            'required': "Необхідно ввести Romania",
        })
    
    Date = forms.CharField(
        label="Date",
        error_messages={
            'required': "Необхідно ввести Date",
        })
    
    Time = forms.CharField(
        label="time",
        error_messages={
            'required': "Необхідно ввести time",
        })
    is_agree = forms.BooleanField(
        help_text="Я приймаю політику конфіденційності сайту",
        error_messages={
            'required': "Ви маєте погодитись з політикою конфіденційності сайту"
        }
    )
    
    def clean(self):                               
        cleaned_data = super().clean()
        if 'index' in cleaned_data :
            index = cleaned_data['index']
            if re.search(r"\D", index):
                self.add_error(
                    "index",
                    ValidationError("index має містити лише цифри"))

        if 'Date' in cleaned_data :
            Date = cleaned_data['Date']
            if re.search(r"^\d{2}\.\d{2}\.\d{4}$", Date):
                self.add_error(
                    "Date",
                    ValidationError("Date має містити лише Date"))
        return cleaned_data