from flask import Flask, render_template, request

app = Flask(__name__)
#connecting MOngoDB
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["college"]
table=db["SIT"]
@app.route("/", methods=["GET","POST"])
def home():
    return render_template("homepage.html")
@app.route(rule="/con",methods=["GET","POST"])
def dbcon():
    fname=" "
    fusn=" "
    sem=" "
    if request.method == "POST":
        fname = request.form.get("name")
        fusn = request.form.get("usn")
        sem = request.form.get("sem")
        data={"name":fname,"usn":fusn,"sem":sem}
        db.table.insert_one(data)
        return "data inserted successfully"
app.run(debug=True)