import uuid
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from slides.models import User, Attachment, Comment, Slide
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


    class Meta:
        model = User
        fields = ("username", "name", "email", "password1", "password2", "image")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
class UpdateUserForm(forms.Form):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload a new profile photo"
        self.fields['name'].label = "Real Name"


    class Meta:
        model = User
        fields = ("name", "email", "image")


class CommentForm(forms.Form):
    slide = None
    text = forms.CharField(widget=forms.Textarea)
    attachments = []

    class Meta:
        model = Comment
        fields = ("text",)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        #unpack slide info from args array, know position for each thing
        print args
        if args:
            self.data['text'] = args[0]['resources'] #resources = name on text field
            print args[1]
            for attachment in args[1]:
                unique_id = str(uuid.uuid4())
                while Attachment.objects.filter(uuid=unique_id).exists():
                    unique_id = str(uuid.uuid4())
                new_attachment = Attachment.objects.create(file=attachment, uuid=unique_id) #change file to attachment.file?
                self.attachments.append(new_attachment)
            self.slide, created = Slide.objects.get_or_create(week_number=args[2], day=args[3], slide_set=args[4], slide_number=args[5], slide_header=args[6], url=args[7])

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.slide = self.slide
        # comment.user = request.user
        for attachment in self.attachments:
            attachment.comment = comment
        if commit:
            comment.save()
            for attachment in self.attachments:
                attachment.save()
        return comment