from django import forms
from .models import Dialect


class DialectCreateForm(forms.ModelForm):
    
    def __init__(self, language, *args, **kwargs):
        # get excluded data or return none
        excluded = kwargs.get('excluded', None)
        # if there take out until not pass itself as super dialect
        if kwargs.__contains__('excluded'):
            kwargs.pop('excluded')
        super(DialectCreateForm, self).__init__(*args, **kwargs)
        # if there exclude will exclude itself to not present in list
        if excluded:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).exclude(pk=excluded.pk).order_by('name')
        else:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).order_by('name')

    class Meta:
        model = Dialect
        fields = ['super_dialect', 'name', 'native_name', 'description']


