from storages.backends.s3boto3 import S3Boto3Storage


class MediaRootS3BotoStorage(S3Boto3Storage):
    location = ''

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        return name
