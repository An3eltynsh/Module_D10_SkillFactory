from django_filters import (FilterSet, DateFilter, ModelMultipleChoiceFilter)
from .models import Post, Category
from django import forms

class PostFilter(FilterSet):

    dtime_p = DateFilter(field_name='dtime_p', widget=forms.DateInput(attrs={'type': 'date'}),
                         lookup_expr='dtime_p__gte')

    category = ModelMultipleChoiceFilter(
        field_name = 'postcategory__category',
        queryset = Category.objects.all(),
        label = 'category'
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            #'dtime_p': ['']
        }

