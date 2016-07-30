from django import forms

from .models import Buffet, Review, Images, LOCATION_CHOICES, CUISINE_CHOICES

class BuffetForm(forms.ModelForm):

    class Meta:
        model = Buffet
        labels = {
            'name': "Name Of Buffet",
            'desc': "Description",
            'cuisine_type' : "Type of cuisine", 
            'hrs_opening' : "Opening Hours **[Please use the following format: HH:MM:SS 24-hour format]** ",
            'hrs_closing' : "Closing Hours **[Please use the following format: HH:MM:SS 24-hour format]** ",
            'weekday_adult_lunch_price' : "Weekday Adult Lunch Price **Compulsory** ",
            'weekday_adult_dinner_price' : "Weekday Adult Dinner Price **Compulsory** ",
            
            'weekend_adult_lunch_price' : "Weekend Adult Lunch Price (in S$) **Compulsory** ",
            'weekend_adult_dinner_price' : "Weekend Adult Dinner Price (in S$) **Compulsory** ",

            'weekday_adult_breakfast_price' : "Weekday Adult Breakfast Price (in S$) ",
            'weekday_adult_hightea_price' : "Weekday Adult High Tea Price (in S$) ",
            
            'weekday_child_breakfast_price' : "Weekday Child Breakfast Price (in S$) ",
            'weekday_child_lunch_price' : "Weekday Child Lunch Price (in S$) ",
            'weekday_child_hightea_price' : "Weekday Child High Tea Price (in S$) ",
            'weekday_child_dinner_price' : "Weekday Child Dinner Price (in S$) ",

            'weekend_adult_breakfast_price' : "Weekend Adult Breakfast Price (in S$) ",
            'weekend_adult_hightea_price' : "Weekend Adult High Tea Price (in S$) ",

            'weekend_child_breakfast_price' : "Weekend Child Breakfast Price (in S$) ",
            'weekend_child_lunch_price' : "Weekend Child Lunch Price (in S$) ",
            'weekend_child_hightea_price' : "Weekend Child High Tea Price (in S$) ",
            'weekend_child_dinner_price' : "Weekend Child Dinner Price (in S$) "

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
                  'weekend_child_dinner_price',
                  )
        
    
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({ 
              'class': 'form-control',
              'placeholder': self.fields[field].label
            })


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment')

class ImageForm(forms.ModelForm):
  image = forms.ImageField(label='Image')
  class Meta:
    model = Images
    fields = ('image',)

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