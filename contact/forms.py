from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(
        attrs={'class':'input-contact','placeholder':'Enter your name'}
    ), min_length=5, max_length=40)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'input-contact', 'placeholder':'Enter your email'}
    ))
    content = forms.CharField(label='Comments', required=True, widget=forms.Textarea(
        attrs={'class':'input-contact-c', 'placeholder':'Enter your comment', 'cols':'15', 'rows':'5'}
    ), min_length=1, max_length=1000)
    terms = forms.BooleanField(label='terms&conditions',required=True, widget=forms.CheckboxInput(
        attrs={'class':'input-contact-t'}
    ))

