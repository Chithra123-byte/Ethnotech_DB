from flask import Flask, render_template, request

app = Flask(__name__)
#connecting MOngoDB
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["college"]
table=db["SIT"]
@app.route("/", methods=["GET","POST"])#program starts from here
def home():
    return render_template("student.html")#fetching the homepage.html file from templates folder
@app.route(rule="/con",methods=["GET","POST"])#insert data into the database
def dbcon():
        fname = request.form.get("name")
        fusn = request.form.get("usn")
        sem = request.form.get("sem")
        marks = int(request.form["marks"])
        data={"name":fname,"usn":fusn,"sem":sem,"marks":marks}
        table.insert_one(data)
        return "data inserted successfully"
@app.route("/studentInfo")
def studentInfo():
    info=table.find({"marks":{"$gt":25}})
    return render_template("show.html",students=info)#passing the data to studentInfo.html file




app.run(debug=True)