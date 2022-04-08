from django import forms


class CreateNewProduct(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    amount_in_stock = forms.DecimalField(max_digits=6, decimal_places=0)
