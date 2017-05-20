from django import forms
from django.forms.fields import Select
from lib.forms import select_options


class PhoneInput(forms.TextInput):
    mask = '(999) 999-9999'

    def build_attrs(self, extra_attrs=None, **kwargs):
        """Helper function for building an attribute dictionary."""
        attrs = super(PhoneInput, self).build_attrs(extra_attrs=extra_attrs, **kwargs)
        attrs['data-mask'] = self.mask
        return attrs


class StateSelect(Select):
    """
    A Select widget that uses a list of U.S. states/territories as its choices.
    """
    def __init__(self, attrs=None):
        super(StateSelect, self).__init__(attrs, choices=select_options.US_STATES_ABBREVIATIONS)