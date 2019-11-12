from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit


class ConfirmForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-secondary', onclick='window.history.back()'))
        self.helper.add_input(Submit('submit', 'Confirm'))
