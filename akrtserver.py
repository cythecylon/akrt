
# http://gouthamanbalaraman.com/blog/minimal-flask-login-example.html
from flask import Flask, Response, render_template
from flask_login import LoginManager, UserMixin, login_required
import os

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    # proxy for a database of users
    user_database = {"JohnDoe": ("JohnDoe", "John"),
               "JaneDoe": ("JaneDoe", "Jane")}

    def __init__(self, username, password):
        self.id = username
        self.password = password

    @classmethod
    def get(cls,id):
        return cls.user_database.get(id)



@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None


@app.route("/",methods=["GET"])
def index():
    return Response(response="Go to [url]:5000/report/woid",status=200)

@app.route("/report/<int:woid>",methods=["GET"])
@login_required
def getreport(woid):
    return Response(response=getwo(woid), status=200)

def getwo(woid):
    with open(str(woid)+".txt","rt") as f:
        values = f.read()
    return values

if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
app.run(port=5000,debug=True)
