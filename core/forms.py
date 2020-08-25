from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'text':forms.Textarea(attrs={'placeholder':'Enter your message here...'}),
            'name':forms.TextInput(attrs={'placeholder':'Name'}),
            'phone':forms.TextInput(attrs={'placeholder':'Phone Number'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email address'}),

        }
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'form-control w-100'
        self.fields['text'].label = ''
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = ''
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''


        