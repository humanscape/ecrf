from django import forms
from .models import Ks
from .assets import RADIO_FIELDS, PREFIX, SUFFIX, CALCULATE_AGE_FIELDS


class KsForm(forms.ModelForm):
    class Meta:
        model = Ks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(KsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            # prefix/suffix custom
            if field in PREFIX['ks'].keys():
                self.fields[field].widget.attrs.update({'prefix': PREFIX['ks'][field]})
            elif field in SUFFIX['ks'].keys():
                self.fields[field].widget.attrs.update({'suffix': SUFFIX['ks'][field]})

            # radio option label custom
            if self.fields[field].required is False and field in RADIO_FIELDS['ks']:
                self.fields[field].choices = tuple([(u'', '-')] + list(self.fields[field].choices)[1:])

            # caculate age field custom
            for key, value in CALCULATE_AGE_FIELDS['ks'].items():
                if field == value:
                    self.fields[field].widget.attrs.update({'target': key})
