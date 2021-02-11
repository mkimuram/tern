import subprocess
from subprocess import check_output
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def exec_tern(image):
    return check_output(['tern', 'report', '-f', 'html', '-i', image]).decode('utf-8')

@app.route('/',methods = ['GET'])
def home():
    return render_template("/index.html")

@app.route('/tern',methods = ['POST', 'GET'])
def tern():
    image = request.args.get('image')
    return exec_tern(image)

if __name__ == "__main__":
    app.run()
