from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button, Fieldset, ButtonHolder, HTML,Fieldset, MultiField, Div
from crispy_forms.bootstrap import TabHolder, Tab, FormActions, StrictButton
from django.utils.translation import gettext_lazy as _
from .models import Produit
from django.conf import settings


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields =['code', 'sigle', 'intitule', 'grn', 'milisime']
        labels = {
            'code': _('Code titre'),
        }
        help_texts = {
            'code': _('Code titre (voir AFPA DI)'),
            'sigle': _('Nom court'),
            'intitule': _('Nom long'),
            'grn': _('Groupe budgetaire'),
            'milisime': _("L'année de validation "),
        }
        error_messages = {
            'code': {
                'max_length': _('Text way too long for your eyes !'),
            },
        }
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        self.fields['code'].required = True
        self.fields['sigle'].required = True
        self.fields['intitule'].required = False
        self.fields['grn'].required = False
        self.fields['milisime'].required = False
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-5'

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_tag = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                'Nouveau Produit',
                'code',
                'sigle',
                'intitule',
                'grn',
                'milisime',
            ),
        ),
        FormActions(
            Submit('save', 'Save', css_class="btn-success"),
            Submit('cancel', 'Cancel'),
        ),

    )