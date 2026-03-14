from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "super_secret_key_for_session"
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

client = MongoClient("mongodb://localhost:27017/")
db = client["product_db"]

users = db["users"]
admins = db["admins"]
products = db["products"]


# HOME
@app.route("/")
def home():
    return render_template("index.html")


# ADMIN REGISTER (only one admin allowed)
@app.route("/admin_register", methods=["GET","POST"])
def admin_register():
    admin_exist = admins.find_one({})
    
    if admin_exist:
        return "Admin already registered!"

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admins.insert_one({
            "username":username,
            "password":password
        })
        return redirect("/login")

    return render_template("admin_register.html")


# USER REGISTER
@app.route("/user_register", methods=["GET","POST"])
def user_register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username":username})
        if user:
            return "User already registered!"

        users.insert_one({
            "username":username,
            "password":password
        })
        return redirect("/login")

    return render_template("user_register.html")


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username":username,"password":password})
        admin = admins.find_one({"username":username,"password":password})

        if user or admin:
            session["username"] = username
            session["role"] = "admin" if admin else "user"
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")
    return render_template("dashboard.html")


# ADD PRODUCT
@app.route("/add_product", methods=["GET","POST"])
def add_product():
    if "username" not in session:
        return redirect("/login")

    if request.method == "POST":
        pid = request.form["pid"]
        name = request.form["name"]
        price = request.form["price"]
        desc = request.form["desc"]
        
        image_path = ""
        if "image" in request.files:
            file = request.files["image"]
            if file.filename != "":
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                image_path = "/static/uploads/" + filename

        products.insert_one({
            "pid":pid,
            "name":name,
            "price":price,
            "desc":desc,
            "image":image_path
        })
        return redirect("/view_product")

    return render_template("add_product.html")


# VIEW PRODUCT
@app.route("/view_product")
def view_product():
    data = products.find()
    return render_template("view_product.html", products=data)


# SHOW PRODUCTS FOR EDIT
@app.route("/edit_products")
def edit_products():
    if "username" not in session:
        return redirect("/login")
    data = products.find()
    return render_template("edit_products.html", products=data)


# EDIT PRODUCT
@app.route("/edit_product/<pid>", methods=["GET","POST"])
def edit_product(pid):
    if "username" not in session:
        return redirect("/login")

    product = products.find_one({"pid":pid})

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        desc = request.form["desc"]
        
        update_data = {
            "name":name,
            "price":price,
            "desc":desc
        }
        
        if "image" in request.files:
            file = request.files["image"]
            if file.filename != "":
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                update_data["image"] = "/static/uploads/" + filename

        products.update_one(
            {"pid":pid},
            {"$set": update_data}
        )
        return redirect("/view_product")

    return render_template("edit_product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)