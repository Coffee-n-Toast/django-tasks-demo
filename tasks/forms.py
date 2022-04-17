from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'textarea'})
        self.fields['status'].widget.attrs.update({'class': 'select'})
        self.fields['month'].widget.attrs.update({'class': 'select'})
