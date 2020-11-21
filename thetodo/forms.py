from django import forms
from .models import Task, Category


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'author')

        widgets = {
            'name': forms.TextInput(attrs={'style': 'color:grey', 'placeholder': 'name'}),
            'author': forms.TextInput(attrs={'value': '', 'id': 'user', 'type': 'hidden'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'body', 'author', 'task_date', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'title'}),
            'body': forms.Textarea(attrs={'class': 'textarea'}),
            'author': forms.TextInput(attrs={'class': 'input_box', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'task_date': forms.TextInput(attrs={'class': 'js-date'}),
            'category': forms.TextInput(attrs={'class': 'input_box', 'value': '', 'id': 'categ_name'}),
        }
