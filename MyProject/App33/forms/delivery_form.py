# Інструментарій Django для роботи з формами
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, date, timedelta, time
import re   # regular expressions

# класи-форми описують склад форм у вигляді спеціальних елементів
class DeliveryForm(forms.Form) :
    first_name = forms.CharField(
        min_length=2, 
        max_length=64, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести ім'я",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 64 символи"
        })
    
    last_name = forms.CharField(
        min_length=2,
        max_length=64,
        label="Прізвище",
        error_messages={
            'required': "Необхідно ввести прізвище",
            'min_length': "Прізвище повинно мати щонайменше 2 символи",
            'max_length': "Прізвище не повинно перевищувати 64 символи"
        })
    
    Street_Address = forms.CharField(
        max_length=128,
        label="Адреса",
        error_messages={
            'required': "Необхідно ввести адресу"
        })
    
    Street_Address_L2 = forms.CharField(
        max_length=128,
        required=False,
        label="Адреса (додатково)")
    
    City = forms.CharField(
        max_length=64,
        label="Місто",
        error_messages={
            'required': "Необхідно ввести місто"
        })
    
    Region = forms.CharField(
        max_length=64,
        label="Область",
        error_messages={
            'required': "Необхідно ввести область"
        })
    
    index = forms.CharField(
        max_length=10,
        label="Поштовий індекс",
        error_messages={
            'required': "Необхідно ввести поштовий індекс"
        })
    
    country = forms.ChoiceField(
        choices=[
            ("ua", "Україна"), 
            ("pl", "Польша"), 
            ("cz", "Чехія")],
        label="Країна",
        error_messages={
            'required': "Необхідно вибрати країну"
        })
    
    Date = forms.DateField(
        label="Дата доставки",
        error_messages={
            'required': "Необхідно ввести дату доставки"
        })
    
    Time = forms.TimeField(
        label="Час доставки",
        error_messages={
            'required': "Необхідно ввести час доставки"
        })
    
    is_agree = forms.BooleanField(
        required=True,
        help_text="Я приймаю умови доставки",
        error_messages={
            'required': "Ви маєте погодитись з умовами доставки"
        })
    
    # Валідація імен та прізвища - починаються з великої літери
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and not first_name[0].isupper():
            raise ValidationError("Ім'я повинно починатися з великої літери")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not last_name[0].isupper():
            raise ValidationError("Прізвище повинно починатися з великої літери")
        return last_name
    
    # Валідація власних назв (місто, область, вулиця) - починаються з великої літери
    def clean_City(self):
        city = self.cleaned_data.get('City')
        if city and not city[0].isupper():
            raise ValidationError("Назва міста повинна починатися з великої літери")
        return city
    
    def clean_Region(self):
        region = self.cleaned_data.get('Region')
        if region and not region[0].isupper():
            raise ValidationError("Назва області повинна починатися з великої літери")
        return region
    
    def clean_Street_Address(self):
        street = self.cleaned_data.get('Street_Address')
        if street and not street[0].isupper():
            raise ValidationError("Назва вулиці повинна починатися з великої літери")
        return street
    
    # Валідація поштового індексу - тільки цифри
    def clean_index(self):
        index = self.cleaned_data.get('index')
        if index and not index.isdigit():
            raise ValidationError("Поштовий індекс повинен складатися тільки з цифр")
        return index
    
    # Валідація дати - має бути у майбутньому, щонайменше через добу
    def clean_Date(self):
        delivery_date = self.cleaned_data.get('Date')
        if delivery_date:
            tomorrow = date.today() + timedelta(days=1)
            if delivery_date < tomorrow:
                raise ValidationError("Дата доставки повинна бути щонайменше через добу від сьогодні")
        return delivery_date
    
    # Валідація часу - має бути в робочому проміжку (9:00-18:00)
    def clean_Time(self):
        delivery_time = self.cleaned_data.get('Time')
        if delivery_time:
            work_start = time(9, 0)
            work_end = time(18, 0)
            if delivery_time < work_start or delivery_time > work_end:
                raise ValidationError("Час доставки повинен бути в робочому проміжку (9:00-18:00)")
        return delivery_time
    
    # Перевірка комбінації дати та часу
    def clean(self):
        cleaned_data = super().clean()
        delivery_date = cleaned_data.get('Date')
        delivery_time = cleaned_data.get('Time')
        
        # Якщо дата сьогодні, перевіряємо, що час ще не минув
        if delivery_date and delivery_time:
            if delivery_date == date.today():
                now = datetime.now().time()
                if delivery_time <= now:
                    raise ValidationError("Час доставки не може бути в минулому")
        
        return cleaned_data