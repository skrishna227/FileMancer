from django import forms
from .models import FileUploadDetail
from filemancer.apps.taskforge.models import TaskAvailableModel

choice_list = []
for dt in TaskAvailableModel.objects.all().values('task_name'):
    choice_list.append((dt['task_name'], dt['task_name']))


class FileUploadForm(forms.ModelForm):
    tasks = forms.MultipleChoiceField(
        choices=choice_list,
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = FileUploadDetail
        fields = ['file']
    
