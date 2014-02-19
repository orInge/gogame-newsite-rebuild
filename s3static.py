from storages.backends.s3boto import S3BotoStorage

class S3Static(S3BotoStorage):
     location = 'static'   
