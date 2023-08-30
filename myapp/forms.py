from django import forms

class FormNewTask(forms.Form):
    title = forms.CharField(label='titulo', max_length=200)
    description = forms.CharField(widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='nombre', max_length=200)
    