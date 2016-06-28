from django import forms

from .models import Buffet, Review

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
        fields = ('name', 
                  'location', 
                  'cuisine_type',
                  'desc', 
                  'hrs_opening', 
                  'hrs_closing', 
                  'address', 
                  'phone_number', 
                  'weekday_adult_breakfast_price',
                  'weekday_adult_lunch_price', 
                  'weekday_adult_hightea_price', 
                  'weekday_adult_dinner_price', 
                  'weekday_child_breakfast_price', 
                  'weekday_child_lunch_price', 
                  'weekday_child_hightea_price', 
                  'weekday_child_dinner_price', 
                  'weekend_adult_breakfast_price', 
                  'weekend_adult_lunch_price',
                  'weekend_adult_hightea_price', 
                  'weekend_adult_dinner_price', 
                  'weekend_child_breakfast_price', 
                  'weekend_child_lunch_price', 
                  'weekend_child_hightea_price', 
                  'weekend_child_dinner_price')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment')