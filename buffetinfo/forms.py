from django import forms

from .models import Buffet

from datetimewidget.widgets import TimeWidget

class BuffetForm(forms.ModelForm):

    class Meta:
        model = Buffet
        widgets = {
            'hrs_opening': TimeWidget(usel10n = True, bootstrap_version=3),
            'hrs_closing': TimeWidget(usel10n = True, bootstrap_version=3),
        }
        labels = {
            'name': "Name Of Place",
            'desc': "Description",
        }
        fields = ('name', 'location', 'desc', 'hrs_opening', 'hrs_closing', 'price', 'child_price')