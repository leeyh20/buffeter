from django.contrib import admin
from .models import Buffet, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('buffet', 'rating', 'comment', 'created_date')
    list_filter = ['created_date', 'author']
    search_fields = ['comment']

admin.site.register(Buffet)

admin.site.register(Review, ReviewAdmin)