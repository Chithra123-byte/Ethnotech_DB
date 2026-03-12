from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
#creation database
db=client["college"]
#creation collection
data1=db["student"]
# #inserting data into collection
# val={"student_id":6,"name":"suresh","age":22,"dep_id":2}
# db.student.insert_one(val)
# print("data inserted successfully")

# #input of user by taking input from user
# student_id=int(input("enter student id:"))
# name=input("enter student name:")
# age=int(input("enter student age:"))    
# dep_id=int(input("enter student dep_id:"))
# val={"student_id":student_id,"name":name,"age":age,"dep_id":dep_id}
# db.student.insert_one(val)
# print("data inserted successfully")
data2=db["department"]
data3=db["marks"]
data4=db["subject"]

# for i in data3.find():
#     if i["marks"] < 80:
#         print(i)


