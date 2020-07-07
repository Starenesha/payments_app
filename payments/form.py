from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['number', 'date', 'amount', 'purpose_of_payment', 'status']

        widgets = {
            'purpose_of_payment': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(),
            # 'date': forms.SelectDateWidget()
        }
#
#
# class PaymentUpdateForm(forms.ModelForm):
#