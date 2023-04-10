from django import forms

shift = (
    ('1','Morning'),
    ('2','Afternoon'),
    ('3','Evening'),
)

class Inputform (forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=shift)
    time_log = forms.TimeField()