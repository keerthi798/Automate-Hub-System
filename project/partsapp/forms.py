from django import forms
from .models import CustomUser
from .models import Vehicle

from .models import Parts
# from .models import ServiceBooking

# class ServiceBookingForm(forms.ModelForm):
#     class Meta:
#         model = ServiceBooking
#         fields = ['user', 'driver_number', 'vehicle_number', 'service_branch', 'vehicle_model', 'service_type', 'service_date', 'email']

class PartForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = ['partsname', 'description', 'price', 'parts_image', 'quantity', 'categories','discount', 'additional_details']
class WorkerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','address','phone_number','password','role']



# class VehicleForm(forms.ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = '__all__'
#         widgets = {
#             'images': forms.FileInput(attrs={'multiple': True}),
#             'vehicle_colors': forms.SelectMultiple(attrs={'class': 'form-control'}),
#         }
class MultipleFileInput(forms.ClearableFileInput):
    def create_input(self, name, data, attrs=None):
        attrs['multiple'] = True
        return super().create_input(name, data, attrs)

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'images': MultipleFileInput(),
            'vehicle_colors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

