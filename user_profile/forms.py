# starting with email_auth's forms as a starting point

from email_auth.models import User as User
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class ProfileForm(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    
    # username = forms.RegexField(regex=r'^[\w.@+-]+$',
    #                             max_length=30,
    #                             label=_("Username"),
    #                             error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    team_name = forms.CharField(label=_("Team Name"))
    
    # clean this up
    # p1_first = forms.CharField(label=_("P1 First Name"))
    # p1_last = forms.CharField(label=_("P1 Last Name"))
    # p1_email = forms.CharField(label=_("P1 Email"))

    # p2_first = forms.CharField(label=_("P2 First Name"))
    # p2_last = forms.CharField(label=_("P2 Last Name"))
    # p2_email = forms.CharField(label=_("P2 Email"))

    # p3_first = forms.CharField(label=_("P3 First Name"))
    # p3_last = forms.CharField(label=_("P3 Last Name"))
    # p3_email = forms.CharField(label=_("P3 Email"))

    # p4_first = forms.CharField(label=_("P4 First Name"))
    # p4_last = forms.CharField(label=_("P4 Last Name"))
    # p4_email = forms.CharField(label=_("P4 Email"))

    # p5_first = forms.CharField(label=_("P5 First Name"))
    # p5_last = forms.CharField(label=_("P5 Last Name"))
    # p5_email = forms.CharField(label=_("P5 Email"))
 
    # it would be better to define a dictionary 
    # players = {}
    # for i in range(1, settings.PLAYERS_PER_TEAM):
    #     players["first_name"+str(i)] = forms.CharField(label=_("First Name"))
    #     players["last_name"+str(i)] = forms.CharField(label=_("Last Name"))
    #     players["email"+str(i)] = forms.EmailField(label=_("Email"))
    
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data