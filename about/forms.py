from django.forms import ModelForm
from django.db import nama

class bathsulmasail(ModelForm):
    class meta :
        model = nama
        fields = '_all_',