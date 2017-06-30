from django import forms
from jobs.models import Position, Comment, Company, Experience
from django.contrib.auth.models import User


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
