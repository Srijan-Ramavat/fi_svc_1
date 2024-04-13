from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('date', 'amount', 'category', 'description')

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == "date":
                field.widget = forms.DateInput(attrs={'type': 'date'})
                field.widget.attrs.update({"class": "form-control datepicker"})
            elif isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field.widget, forms.NumberInput):
                field.widget.attrs.update({"class": "form-control"})