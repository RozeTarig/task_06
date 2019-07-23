from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        # fields=['field_1', 'field_2', 'field_3']
        fields = '__all__'
