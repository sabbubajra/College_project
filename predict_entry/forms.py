from django.forms import ModelForm
from .models import Predict

class predict_form(ModelForm):
    class Meta:
        model = Predict
        fields = '__all__'