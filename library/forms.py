from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Book, Page


class BookCreateForm(forms.ModelForm):
    location = forms.CharField(error_messages={'required': 'this field is required'})
    publisher = forms.CharField(error_messages={'required': 'this field is required'})
    genres = forms.CharField(error_messages={'required': 'this field is required'})
    languages = forms.CharField(error_messages={'required': 'this field is required'})
    writers = forms.CharField(error_messages={'required': 'this field is required'})
    '''
    def __init__(self, language, *args, **kwargs):
        # get excluded data or return none
        excluded = kwargs.get('excluded', None)
        # if there take out until not pass itself as super dialect
        if kwargs.__contains__('excluded'):
            kwargs.pop('excluded')
        super(BookCreateForm, self).__init__(*args, **kwargs)
        # if there exclude will exclude itself to not present in list
        
        if excluded:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).exclude(id__in=excluded).order_by('name')
        else:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).order_by('name')
    '''

    class Meta:
        model = Book
        fields = ['name', 'writers', 'genres', 'languages', 'location', 'publisher', 'page_quantity', 'is_copyright',
                  'image', 'description', 'edition_number', 'volume', 'part']

    '''
    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(BookCreateForm, self).clean()
        # extract the name from the data
        name = self.cleaned_data.get('name')
        # conditions to be met for the name unique
        if Dialect.objects.filter(name=name).exists():
            self._errors['name'] = self.error_class([_('Dialect with this Dialect Name already exists.')])
        # return any errors if found
        return self.cleaned_data
    '''


class PageCreateForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['number', 'page_type', 'is_blank', 'is_finished', 'image', 'preview_page',]
