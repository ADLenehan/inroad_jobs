from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        return self.location + name


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION

    # def _clean_name(self, name):
    #     return name
    #
    # def _normalize_name(self, name):
    #     return name

