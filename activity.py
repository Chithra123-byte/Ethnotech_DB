from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
#creation database
db=client["college"]
#creation collection
data1=db["student"]
data2=db["department"]
data3=db["marks"]
data4=db["subject"]


print("1)Add \n 2)Delete \n 3)Display\n")
option=int(input("Enter your option:"))
if option==1:
    print("For which collection you want to add data: \n 1) student \n 2)department \n 3) marks \n 4) subject\n ")
    collection=int(input("Enter your collection:"))
    if collection==1:
        student_id=int(input("enter Student id:"))
        name=input("enter Student name:")
        age=int(input("Enter student age:"))
        dep_id=int(input("Enter dep id:"))
        val={"student_id":student_id,"name":name,"age":age,"dep_id":dep_id}
        db.student.insert_One(val)
    elif collection==2:
        dep_id=int(input("enter department id:"))
        dept_name=input("enter department name")
        val={"dep_id":dep_id,"dept_name":dept_name}
        db.department.insert_One(val)
    elif collection==3:
        s_id=int(input("enter student id:"))
        subject_id=int(input("enter subject id:"))
        marks=int(input("Enter subject marks:"))
        val={"s_id":s_id,"subject_id":subject_id,"marks":marks}
        db.department.insert_One(val)
    elif collection==4:
        s_id=int(input("enter student id:"))
        sub_name=input("enter sub name:")
        val={"s_id":s_id,"sub_name":sub_name}
        db.department.insert_One(val)
    else:
        print("invalid choice!")
elif option==2:
     print("For which collection you want to delete data: \n 1) student \n 2)department \n 3) marks \n 4) subject\n ")
     collection=int(input("Enter your collection:"))
     if collection==1:
        student_id=int(input("enter Student id:"))
        name=input("enter Student name:")
        age=int(input("Enter student age:"))
        dep_id=int(input("Enter dep id:"))
        val={"student_id":student_id,"name":name,"age":age,"dep_id":dep_id}
        db.student.delete_One(val)
     elif collection==2:
        dep_id=int(input("enter department id:"))
        dept_name=input("enter department name")
        val={"dep_id":dep_id,"dept_name":dept_name}
        db.department.delete_One(val)
     elif collection==3:
        s_id=int(input("enter student id:"))
        subject_id=int(input("enter subject id:"))
        marks=int(input("Enter subject marks:"))
        val={"s_id":s_id,"subject_id":subject_id,"marks":marks}
        db.department.delete_One(val)
     elif collection==4:
        s_id=int(input("enter student id:"))
        sub_name=input("enter sub name:")
        val={"s_id":s_id,"sub_name":sub_name}
        db.department.delete_One(val)
     else:
        print("invalid choice!")
elif option==3:
    print("For which collection you want to delete data: \n 1) student \n 2)department \n 3) marks \n 4) subject\n ")
    collection=int(input("Enter your collection:"))
    if collection==1:
        for i in data1.find():
            print(i)
    elif collection==2:
        for i in data2.find():
            print(i)
    elif collection==3:
        for i in data3.find():
            print(i)
    elif collection==4:
        for i in data4.find():
            print(i)
    else:
        print("invalid choice")
    
    

    
    
