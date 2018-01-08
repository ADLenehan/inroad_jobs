from django import forms
from jobs.models import Position, Comment, Company, Experience, Board, Application
from django.contrib.auth.models import User


class BoardForm(forms.ModelForm):
    slug = forms.SlugField(max_length=100, help_text="Slug", required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.Textarea()
    logo = forms.ImageField(required=False)

    class Meta:
        model = Board
        fields = ['slug', 'title', 'description','logo']

    def __str__(self):
        return self.title


class PositionForm(forms.ModelForm):
    companies = Company.objects.all()
    experiences = Experience.objects.all()
    company = forms.ModelChoiceField(queryset=companies,help_text="Company", required=False)
    experience = forms.ModelChoiceField(queryset=experiences,help_text="Experience", required=False)
    indeed_id = forms.CharField(max_length=16, help_text="Indeed ID", required=False)
    job_title = forms.CharField(max_length=1000, help_text="Job Title", required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    url = forms.CharField(max_length=200, help_text="Please enter the URL of the job.", required=False)
    city = forms.CharField(max_length=125, help_text="City", required=False)
    state = forms.CharField(max_length=125, help_text="State", required=False)

    class Meta:
        model = Position
        fields = ['company', 'experience', 'indeed_id', 'job_title', 'description', 'url', 'city', 'state']

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['company_site_url'] = url
        return cleaned_data


class CommentForm(forms.ModelForm):
    companies = Company.objects.all()
    company = forms.ModelChoiceField(queryset=companies,help_text="Company", required=False)
    user_position = forms.CharField(max_length=200, help_text="User Position", required=True)
    picture_url = forms.CharField(max_length=200, help_text="Photo URL", required=False)
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['company','user_position','picture_url','text']

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['company_site_url'] = url
        return cleaned_data


class ApplicationForm(forms.ModelForm):
    question1 = forms.Textarea()
    question2 = forms.Textarea()

    class Meta:
        model = Application
        exclude = ['user', 'position', 'checked', 'fit']