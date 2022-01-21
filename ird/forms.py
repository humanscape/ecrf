from django import forms
from .models import Ird, IrdHistory
from .assets import RADIO_FIELDS, CALCULATE_AGE_FIELDS


class IrdForm(forms.ModelForm):
    class Meta:
        model = Ird
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IrdForm, self).__init__(*args, **kwargs)
        
        # radio option label custom
        for field in self.fields:
            if self.fields[field].required is False and field in RADIO_FIELDS['ird']:
                self.fields[field].choices = tuple([(u'', '-')] + list(self.fields[field].choices)[1:])


class IrdHistoryForm(forms.ModelForm):
    class Meta:
        model = IrdHistory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IrdHistoryForm, self).__init__(*args, **kwargs)

        # radio option label custom
        for field in self.fields:
            if self.fields[field].required is False and field in RADIO_FIELDS['ird_history']:
                self.fields[field].choices = tuple([(u'', '-')] + list(self.fields[field].choices)[1:])

            # caculate age field custom
            for key, value in CALCULATE_AGE_FIELDS['ird_history'].items():
                if field == value:
                    self.fields[field].widget.attrs.update({'target': key})
                    if value != 'birthdate':
                        self.fields[field].widget.attrs.update({'isyear': 'true'})