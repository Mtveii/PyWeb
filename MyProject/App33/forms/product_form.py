from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Назва")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Ціна")
    description = forms.CharField(widget=forms.Textarea, label="Опис")
    quantity = forms.IntegerField(min_value=0, label="Кількість")

