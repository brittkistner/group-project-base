from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.core.exceptions import ValidationError
=======
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
from slides.models import User
from django import forms


class UserForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload a new profile photo"
        self.fields['name'].label = "Real Name"
<<<<<<< HEAD
=======
        #upload a new profile photo
        #real name
        #request username or set email as username
        #email
        #password
        #confirm password

>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e

    class Meta:
        model = User
        fields = ("username", "name", "email", "password1", "password2", "image")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
<<<<<<< HEAD
<<<<<<< HEAD
            print "in try"
=======
>>>>>>> 3df0dd3c1f6a1d97da3ac75855aeb43aa748a463
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError(
=======
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise User.ValidationError(
>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

<<<<<<< HEAD
class CommmentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    attachments = forms.FileField()
=======
# class CommmentForm(forms.Form):

>>>>>>> 9c229482c3db6da2a0e64378b2eaa028acd67e3e
