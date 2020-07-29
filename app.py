from flask import Flask,request
import jwt

app = Flask(__name__)
key ="this is a secret key for encryption"
@app.route('/')
def index():
    return("<b>Welcome, send post request <a href='/login'>here</a> to check api")
@app.route("/login", methods=["POST"])
def login():
    if not (request.form['email'] and request.form['password']):
        return("<b>pass email and password</b>")
    auth = jwt.encode({"auth":request.form['email'],"email":request.form['password']},key, algorithm="HS256")
    value = auth.decode('utf-8')
    return("Authentication code is <p><b>{}</b></p>".format(value))

@app.route('/verify')
def verify():
    if not request.args.get('code'):
        return("<b> pass token as code</b>")
    auth = jwt.decode(request.args.get('code'),key)
    return(auth)


if __name__ == "__main__":
    app.run()