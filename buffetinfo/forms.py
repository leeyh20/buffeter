from django import forms

from .models import Buffet, Review, LOCATION_CHOICES, CUISINE_CHOICES

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
            'cuisine_type' : "Type of cuisine"
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


class FilterForm(forms.Form):
    location = forms.CharField(required=False, label='Location (MRT Station)', widget=forms.Select(choices=LOCATION_CHOICES, attrs={'onChange': 'this.form.submit();'}))
    cuisine_type = forms.CharField(required=False, label='Type of Cuisine', widget=forms.Select(choices=CUISINE_CHOICES, attrs={'onChange': 'this.form.submit();'}))
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        if not self.fields['cuisine_type'].widget.choices[0][0] == '':
            self.fields['cuisine_type'].widget.choices.insert(0, ('','---------' ) )
        if not self.fields['location'].widget.choices[0][0] == '':
            self.fields['location'].widget.choices.insert(0, ('','---------' ) )
    #price_twenty = forms.BooleanField(required=False, label='Price less than 20')