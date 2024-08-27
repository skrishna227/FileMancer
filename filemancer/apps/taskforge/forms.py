from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()
    tasks = forms.MultipleChoiceField(
        choices=[
            ('backup', 'Backup File'),
            ('data_entry', 'Data Entry'),
            ('cleanup', 'File Cleanup')
        ],
        widget=forms.CheckboxSelectMultiple,
    )
