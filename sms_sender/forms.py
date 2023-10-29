from django import forms


class SMSSendForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефону', max_length=15, help_text='Наприклад: +1234567890')