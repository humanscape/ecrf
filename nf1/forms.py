from django import forms
from .models import Crf
from .assets import RADIO_FIELDS, PREFIX, SUFFIX, CALCULATE_AGE_FIELDS


class CrfsForm(forms.ModelForm):

    class Meta:
        model = Crf
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CrfsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            # prefix/suffix custom
            if field in PREFIX['crf'].keys():
                self.fields[field].widget.attrs.update({'prefix': PREFIX['crf'][field]})
            elif field in SUFFIX['crf'].keys():
                self.fields[field].widget.attrs.update({'suffix': SUFFIX['crf'][field]})

            # radio option label custom
            if self.fields[field].required is False and field in RADIO_FIELDS['crf']:
                self.fields[field].choices = tuple([(u'', '-')] + list(self.fields[field].choices)[1:])
            
            # caculate age field custom
            for key, value in CALCULATE_AGE_FIELDS['crf'].items():
                if field == value:
                    self.fields[field].widget.attrs.update({'target': key})
                