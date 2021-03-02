from django import forms
from .models import *


global form_labels, form_fields
form_labels = {
    'code': 'Code',
    'name_en': 'Name',
    'name_lc': 'नाम',
    'display_order': 'Display Order',
}

form_fields = ('code', 'name_en', 'name_lc', 'display_order')


class ProvinceForm(forms.ModelForm):

    class Meta:
        model = Province
        fields = form_fields
        labels = form_labels


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = form_fields[:1]+('province_id',)+form_fields[1:]
        form_labels.update({'province_id': 'Province'})
        labels = form_labels

    def __init__(self, *args, **kwargs):
        super(DistrictForm, self).__init__(*args, **kwargs)
        self.fields['province_id'].empty_label = "Select Province"


class LocalLevelTypeForm(forms.ModelForm):
    class Meta:
        model = LocalLevelType
        fields = form_fields
        labels = form_labels


class LocalLevelForm(forms.ModelForm):

    class Meta:
        model = LocalLevel
        fields = form_fields[:1]+('district_id',
                                  'local_level_type_id')+form_fields[1:]
        fields = fields[:5]+('wards_count', 'gps_lat', 'gps_long')+fields[5:]

        form_labels.update({'district_id': 'District',
                            'local_level_type_id': 'Local Level Type',
                            'wards_count': 'Wards Count',
                            'gps_lat': 'GPS Latitude',
                            'gps_long': 'GPS Longitude'})
        labels = form_labels

    def __init__(self, *args, **kwargs):
        super(LocalLevelForm, self).__init__(*args, **kwargs)
        self.fields['district_id'].empty_label = "Select District"
        self.fields['local_level_type_id'].empty_label = "Select Locallevel Type"


class FiscalYearForm(forms.ModelForm):

    class Meta:
        model = FiscalYear
        fields = ('code', 'from_date_bs', 'from_date_ad',
                  'to_date_bs', 'to_date_ad', 'display_order')
        form_labels.update({'from_date_bs': 'From Date(B.S)',
                            'from_date_ad': 'From Date(A.D)',
                            'to_date_bs': 'To Date(B.S)',
                            'to_date_ad': 'To Date(A.D)'})
        labels = form_labels
        widgets = {
            'from_date_bs': forms.TextInput(attrs={'id': 'from_date_bs', 'relatedId': 'from_date_ad', 'placeholder': 'yyyy-mm-dd', 'onclick': 'fieldDateChange(this)'}),
            'to_date_bs': forms.TextInput(attrs={'id': 'to_date_bs', 'relatedId': 'to_date_ad', 'placeholder': 'yyyy-mm-dd', 'onclick': 'fieldDateChange(this)'}),
            'from_date_ad': forms.DateInput(attrs={'id': 'from_date_ad', 'type': 'date'}),
            'to_date_ad': forms.DateInput(attrs={'id': 'to_date_ad', 'type': 'date'})
        }


class NepaliMonthForm(forms.ModelForm):

    class Meta:
        model = NepaliMonth
        fields = form_fields
        labels = form_labels


class GenderForm(forms.ModelForm):

    class Meta:
        model = Gender
        fields = form_fields
        labels = form_labels
