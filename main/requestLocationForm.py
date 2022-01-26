from dataclasses import fields
from django import forms
from django import forms
from .models import CommonPlace


class LocationForm(forms.ModelForm):
    class Meta:
        model = CommonPlace
        fields = ['plcae_name', 'lat', 'lat',
                  'phone', 'road_address', 'rate', 'info']
        labels = {
            'lat': '경도',
            'lng': '위도',
        }
