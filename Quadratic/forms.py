from django import forms

class q(forms.Form):
	a = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value for a'}))
	b = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value for b'}))
	c = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value for c'}))
	