from django import forms

class IrisForm(forms.Form):
    sepal_length = forms.FloatField(
        max_value=20,
        min_value=0,
        label="Sepal Length",
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded',
            'placeholder': 'Enter Sepal Length'
        })
    )
    sepal_width = forms.FloatField(
        max_value=20,
        min_value=0,
        label="Sepal Width",
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded',
            'placeholder': 'Enter Sepal Width'
        })
    )
    petal_length = forms.FloatField(
        max_value=20,
        min_value=0,
        label="Petal Length",
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded',
            'placeholder': 'Enter Petal Length'
        })
    )
    petal_width = forms.FloatField(
        max_value=20,
        min_value=0,
        label="Petal Width",
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded',
            'placeholder': 'Enter Petal Width'
        })
    )
