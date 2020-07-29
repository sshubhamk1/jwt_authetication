from flask import Flask,request
import jwt
import os

app = Flask(__name__)
key ="this is a secret key for encryption"
@app.route('/')
def index():
    return("<b>Welcome, send post request <a href='/login'>here</a> to check api")
@app.route("/login/", methods=["POST","GET"])
def login():
    email ="dummy@email"
    password= "dummy password"
    if request.method == "POST":
        if request.form['email']:
            email = request.form['email']
        if request.form['password']:
            password = request.form['password']
    else:
        if request.args.get('email'):
            email = request.args.get('email')
        if request.args.get('password'):
            password = request.args.get('password')
    auth = jwt.encode({"email":email,"password":password},key, algorithm="HS256")
    value = auth.decode('utf-8')
    return("<p>Authentication code is <br><b>{}</b><br>email:{}<br>password:{}</p> see it in verify as <a href='../verify?code={}'>here</a>".format(value,email,password,value))

@app.route('/verify')
def verify():
    if not request.args.get('code'):
        return("<b> pass token as code</b>")
    auth = jwt.decode(request.args.get('code'),key)
    return(auth)


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True)