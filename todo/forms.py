from django.forms import DateInput, ModelForm
from .models import Todo

class TodoForm(ModelForm):
    
    class Meta:
        model = Todo
        exclude = ('fecha',)
        widgets = {
            'fecha_estimada': DateInput(attrs= {'type': 'date'}),
        }
