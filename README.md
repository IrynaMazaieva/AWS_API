# AWS_API
Simple API to access AWS S3 storage.

To use this app you need to have AWS account and S3 bucket. [Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) is tutorial how you could do this.<br>

Install all dependencies with `pipenv install`<br>

Change name of bucket to yours if it is needed(in `application.py` `BUCKET = "myfirstownbucket"`).<br>
If you want to add not only binary files add new extension to tuple of extensions in `application.py` `EXTENSIONS = (".bin", )`.<br>

Start app and go to http://127.0.0.1:5000/ . If you see 'Hello World!' - everything is fine.<br>

http://127.0.0.1:5000/storage - get list of all files in storage.<br>
http://127.0.0.1:5000/upload (only for PUT method) - upload new file to storage.<br>
http://127.0.0.1:5000/download/<filename> - get some file by its key.
