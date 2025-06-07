from django import forms
from .models import Car, Maintenance

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'color', 'vin']

class CarColorForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'vin', 'color']  # Use for 'edit color' only

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set other fields as readonly
        for field_name in ['make', 'model', 'year', 'vin']:
            self.fields[field_name].widget.attrs['readonly'] = True
            self.fields[field_name].widget.attrs['class'] = 'form-control-plaintext'

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'service_type', 'notes', 'cost']
