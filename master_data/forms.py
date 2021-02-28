from django import forms
from .models import *

class ProvinceForm(forms.ModelForm):

    class Meta:
        model = Province
        fields = '__all__'
      

class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(DistrictForm, self).__init__(*args, **kwargs)
        self.fields['province_id'].empty_label = "Select Province"


class LocalLevelForm(forms.ModelForm):
    
    class Meta:
        model = LocalLevel
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(LocalLevelForm, self).__init__(*args, **kwargs)
        self.fields['district_id'].empty_label = "Select District"
        self.fields['local_level_type_id'].empty_label = "Select Locallevel Type"

class LocalLevelTypeForm(forms.ModelForm):
    
    class Meta:
        model = LocalLevelType
        fields = '__all__'        


class FiscalYearForm(forms.ModelForm):
    
    class Meta:
        model = FiscalYear
        fields = '__all__'
        

class NepaliMonthForm(forms.ModelForm):
    
    class Meta:
        model = NepaliMonth
        fields = '__all__'

class GenderForm(forms.ModelForm):
    
    class Meta:
        model = Gender
        fields = '__all__'       