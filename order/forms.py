from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        if not phone.startswith('+996'):
            raise forms.ValidationError('NUmber should start with +996')
        if len(phone) != 13:
            raise forms.ValidationError('Invalid phone number')
        return phone

    def save(self, commit=True):
        order = Order.objects.create(**self.cleaned_data)
        return order
