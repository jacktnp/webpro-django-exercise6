from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from record.models import Record
#from django.contrib.auth.models import User
import datetime

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        exclude = ('approve_status', 'create_by')
        widgets = {
            'title': forms.Textarea(),
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'เนื่องจาก',
            'type': 'ประเภท',
            'start_date': 'ตั้งแต่วันที่:',
            'end_date': 'ถึงวันที่:',
        }
    
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(RecordForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = True
        self.fields['type'].required = False

    def clean(self):
        data = super().clean()

        start = data.get('start_date')
        end = data.get('end_date')

        if start > end:
            self.error = 'End date cannot come before start date'
            raise ValidationError('กรุณากรอกวันที่ให้ถูกต้อง')
        elif start < datetime.datetime.now().date():
            self.error = 'Please do not fill date in past'
            raise ValidationError('กรุณากรอกวันที่ให้ถูกต้อง')
