from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
import aesEnc

UPLOAD_FOLDER = 'D:/PROJECTS__/Qtuxathon/flask/uploaded/'
Encrypted_path = 'D:/PROJECTS__/Qtuxathon/flask/encrypted/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ENC_PATH'] = Encrypted_path


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    if username == 'test' and password == 'test':
        return redirect(url_for('dashboard'))
        #return("LOL")
    else:
        print(username,password)
        return ("Login failed. Please try again.")
    
@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

@app.route('/encrypt')
def upload():
    return render_template('upload.html')

@app.route('/encryption', methods=['GET','POST'])
def encryption():
    if request.method == 'POST': 
        file = request.files['file']  
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('download_file', name=filename))
        print(app.config['UPLOAD_FOLDER'])
        aesEnc.encrypt_large_file(str(app.config['UPLOAD_FOLDER'])+str(filename),Encrypted_path+str(filename)+"_enc")
        return send_from_directory(app.config['ENC_PATH'],(str(filename)+"_enc"))
        #return("Uploaded Successfully")


    
@app.route('/uploaded/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)