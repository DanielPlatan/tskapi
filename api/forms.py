from django import forms

class MtrxValidationForm(forms.Form):
    channel = forms.CharField(required=False)
    os = forms.CharField(required=False)
    date_of = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    country = forms.CharField(required=False)
    impressions = forms.IntegerField(required=False)
    clicks = forms.IntegerField(required=False)
    installs = forms.IntegerField(required=False)
    spend = forms.FloatField(required=False)
    revenue = forms.FloatField(required=False)
    order_by = forms.CharField(required=False)
    group_by = forms.CharField(required=False)
    sort = forms.CharField(required=False)