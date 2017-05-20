from dal import autocomplete
from jobs.models import Company


class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Company.objects.none()

        qs = Company.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs