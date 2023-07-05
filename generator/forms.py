from django import forms

class SettingsPassword(forms.Form):
    num = forms.IntegerField(label='Input numbers', required=True)
    uppercase = forms.BooleanField(required=False)
    lowercase = forms.BooleanField(required=False)
    numbers = forms.BooleanField(required=False)
    symbols = forms.BooleanField(required=False)


class RangeOfNumbers(forms.Form):
    max_num = forms.FloatField(label='Max number', required=False)
    min_num = forms.FloatField(label='Min number', required=False)
    numbers = forms.IntegerField(label='Number of numbers', required=False)
    decimal_places = forms.IntegerField(label='Decimal_places')
    float_or_int = forms.BooleanField(required=False)