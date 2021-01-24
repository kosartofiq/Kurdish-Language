from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Dialect


class DialectCreateForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required': 'this field is required'})
    
    def __init__(self, language, *args, **kwargs):
        # get excluded data or return none
        excluded = kwargs.get('excluded', None)
        # if there take out until not pass itself as super dialect
        if kwargs.__contains__('excluded'):
            kwargs.pop('excluded')
        super(DialectCreateForm, self).__init__(*args, **kwargs)
        # if there exclude will exclude itself to not present in list
        if excluded:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).exclude(id__in=excluded).order_by('name')
        else:
            self.fields['super_dialect'].queryset = Dialect.objects.filter(language=language).order_by('name')

    class Meta:
        model = Dialect
        fields = ['super_dialect', 'name', 'native_name', 'description']

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(DialectCreateForm, self).clean()
        # extract the name from the data
        name = self.cleaned_data.get('name')
        # conditions to be met for the name unique
        if Dialect.objects.filter(name=name).exists():
            self._errors['name'] = self.error_class([_('Dialect with this Dialect Name already exists.')])
        # return any errors if found
        return self.cleaned_data


