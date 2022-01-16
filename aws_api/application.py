from flask import Flask, request, redirect, send_file
from utils import list_files, upload_file, download_file, validate_file_type
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "myfirstownbucket"  # insert you bucket name here
EXTENSIONS = (".bin", )  # add valid extensions here


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    return {'files': list_files(BUCKET)}


@app.route("/upload", methods=['PUT'])
def upload():
    f = request.files['file']
    if validate_file_type(f.filename, EXTENSIONS):
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload_file(f"uploads/{f.filename}", BUCKET)
        return redirect('/storage')
    else:
        return f"File '{f.filename}' has wrong extension. Must be: {EXTENSIONS}"


@app.route("/download/<string:filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)
        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
