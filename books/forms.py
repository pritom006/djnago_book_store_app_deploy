from django import forms
from books.models import Review


class ReveiwForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': "border rounded p-2 w-full", 'placeholder': "Write your review"}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']
        widgets = {'body': forms.Textarea(
            attrs={'class': "border rounded p-2 w-full", 'placeholder': "Write your review"})}
