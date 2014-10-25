from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from slides.models import User


class UserForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload a new profile photo"
        self.fields['name'].label = "Real Name"
        #upload a new profile photo
        #real name
        #request username or set email as username
        #email
        #password
        #confirm password


    class Meta:
        model = User
        fields = ("username", "name", "email", "password1", "password2", "image")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise User.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )