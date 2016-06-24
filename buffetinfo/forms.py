from django import forms

from .models import Buffet

class BuffetForm(forms.ModelForm):

    class Meta:
        model = Buffet
        fields = ('name', 'location', 'desc', 'hrs_opening', 'hrs_closing', 'price', 'child_price')
        #to do, find out how to limit location to a list and limit hrs opening and closing  etc