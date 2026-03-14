from flask import Flask,render_template,request
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["users"]

# Home Page
@app.route("/")
def home():
    return render_template("nav.html")
# Register Page
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # check if username already exists
        existing_user = collection.find_one({"username": username,"email":email})
        if existing_user:
            return "Username already registered"
        else:
            data = {
                "username": username,
                "email": email,
                "password": password
            }
            collection.insert_one(data)
            return "Registration Successful"
    return render_template("register.html")
# Login Page
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        user=collection.find_one({
            "username":username,
            "password":password
        })
        if user:
            return render_template("success.html")
        else:
            return "Invalid Credentials"

    return render_template("login.html")
app.run(debug=True)