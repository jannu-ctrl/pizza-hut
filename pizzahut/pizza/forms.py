from django import forms
from .models import Pizza
# class PizzaForm(forms.Form): #django form class
#     topping1=forms.CharField(label='Topping1',max_length=100)
#     topping2 = forms.CharField(label='Topping2',max_length=100)
#     size=forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
class PizzaForm(forms.ModelForm):
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=10)