from django import forms

class DateForm(forms.Form):
    date = forms.DateField(
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
