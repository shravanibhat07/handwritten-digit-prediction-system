from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def abc(request):
    return render(request,"abc.html")

def led(request):
    return render(request,"led.html")

def predict1(request):
    if(request.method=="POST"):
        data=request.POST
        hours=float(data.get('texthours'))
        age=int(data.get('textage'))
        internet=int(data.get('textinternet'))
        if('buttonadd' in request.POST):
            import pandas as pd
            path="C:\\Users\\SHRAVANI\\OneDrive\\Desktop\\MACHINE LEARNING\\Data\\Data\\Exammarks.csv"
            data=pd.read_csv(path)
            medianvalue=data.hours.median()
            data.hours=data.hours.fillna(medianvalue)
            inputs=data.drop('marks',axis=1)
            output=data.drop(['hours','age','internet'],axis=1)
            import sklearn
            from sklearn import linear_model
            model=linear_model.LinearRegression()
            model.fit(inputs,output)
            result=model.predict([[hours,age,internet]])
            return render(request,'predict1.html',context={'result':"Marks="+str(result[0][0])})

def recognition(request):

    if(request.method=="POST"):

        data=request.POST

        pixel0=int(data.get('pixel0'))
        pixel1=int(data.get('pixel1'))
        pixel2=int(data.get('pixel2'))
        pixel3=int(data.get('pixel3'))
        pixel4=int(data.get('pixel4'))

        if('buttonpredict' in request.POST):

            import pandas as pd
            path="C:\\Users\\SHRAVANI\\OneDrive\\Desktop\\MACHINE LEARNING\\Data\\Data\\digit.csv"
            data=pd.read_csv(path)

            inputs=data.drop('label',axis=1)
            outputs=data['label']

            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,train_size=0.8,random_state=0)

            from sklearn.ensemble import RandomForestClassifier
            model=RandomForestClassifier(n_estimators=10)

            model.fit(x_train,y_train)

            pixels=[pixel0,pixel1,pixel2,pixel3,pixel4] + [0]*779

            result=model.predict([pixels])

            return render(request,'recognition.html',{'result':"Predicted Digit = "+str(result[0])})

    return render(request,'recognition.html')

def index(request):
    return render(request,"index.html")
def counter(request):
    if (request.method=="POST"):
        data=request.POST
        result=data.get("result")
        if result=="":
            result=0
        else:
            result=int(data.get("result"))

        if("increment" in request.POST):
            result=result+1
            return render(request,"counter.html",context={"result":result})  
        if("decrement" in request.POST):
            result=result-1
            return render(request,"counter.html",context={"result":result})
        if("reset" in request.POST):
            result=0
            return render(request,"counter.html",context={"result":result})          
    return render(request,"counter.html")


def calculator(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get("firstnumber"))
        secondnumber=int(data.get("secondnumber"))
        if ("buttonadd" in request.POST):
            result=firstnumber+secondnumber
            return render(request,"calculator.html",context={"result":"Sum= "+str(result)})
        if ("buttonsub" in request.POST):
            result=firstnumber-secondnumber
            return render(request,"calculator.html",context={"result":"SUB= "+str(result)})
        if ("buttonmul" in request.POST):
            result=firstnumber*secondnumber
            return render(request,"calculator.html",context={"result":"MUL= "+str(result)})
        if ("buttondiv" in request.POST):
            result=firstnumber/secondnumber
            return render(request,"calculator.html",context={"result":"DIV= "+str(result)})
    return render(request,"calculator.html")   

def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get("firstnumber"))
        secondnumber=int(data.get("secondnumber"))
        if ("buttonadd" in request.POST):
            result=firstnumber+secondnumber
            return render(request,"calculator.html",context={"result":"Sum= "+str(result)})
        if ("buttonsub" in request.POST):
            result=firstnumber-secondnumber
            return render(request,"calculator.html",context={"result":"SUB= "+str(result)})
        if ("buttonmul" in request.POST):
            result=firstnumber*secondnumber
            return render(request,"calculator.html",context={"result":"MUL= "+str(result)})
        if ("buttondiv" in request.POST):
            result=firstnumber/secondnumber
            return render(request,"calculator.html",context={"result":"DIV= "+str(result)})
        if("buttonavg" in request.POST):
            result=(firstnumber+secondnumber)/2
            return render(request,"calci.html",context={"result":"AVG= "+str(result)})
        if("buttonper" in request.POST):
            result=(firstnumber/secondnumber)*100
            return render(request,"calci.html",context={"result":"PER= "+str(result)})

    return render(request,"calci.html")   



def Employee(request):
    if (request.method=="POST"):
        data=request.POST
        emp_name=data.get("employeename")
        emp_des=data.get("employeedesignation")
        emp_place=data.get("employeeplace")
        Employee_Table.objects.create(EMP_NAME=emp_name,EMP_DES=emp_des,EMP_PLACE=emp_place)
        result="Employee details saved"
        return render(request,"Employee.html",context={"result":result})
    return render(request,"Employee.html")


def Employee1(request):
    if (request.method=="POST"):
        data=request.POST
        emp_name=data.get("employeename")
        emp_des=data.get("employeedesignation")
        emp_place=data.get("employeeplace")
        emp_sal=data.get("employeesalary")
        emp_phno=data.get("employeephonenumber")
        Employee_Table1.objects.create(EMP_NAME=emp_name,EMP_DES=emp_des,EMP_PLACE=emp_place,EMP_SALARY=emp_sal,EMP_PHNO=emp_phno)
        result="Employee details saved"
        return render(request,"Employee1.html",context={"result":result})
    return render(request,"Employee1.html")


def student(request):
    if (request.method=="POST"):
        data=request.POST
        stu_name=data.get("studentname")
        stu_usn=data.get("studentusn")
        stu_sem=data.get("studentsem")
        stu_email=data.get("studentemail")
        
        Student.objects.create(STU_NAME=stu_name,STU_USN=stu_usn,STU_SEM=stu_sem,STU_EMAIL=stu_email)
        result="Student details saved"
        return render(request,"student.html",context={"result":result})
    return render(request,"student.html")

def Employee_View(request):
    getEmployee=Employee_Table.objects.all()
    return render(request,"Employee_View.html",context={"getEmployee":getEmployee})

def Employee_update(request,id):
    getEmployee=Employee_Table.objects.get(id=id)
    if (request.method=="POST"):
        data=request.POST
        empname=data.get("employeename")
        empdes=data.get("employeedesignation")
        empplace=data.get("employeeplace")
        getEmployee.EMP_NAME=empname
        getEmployee.EMP_DES=empdes
        getEmployee.EMP_PLACE=empplace
        getEmployee.save()
        return redirect("/Employee_View/")
    return render(request,"Employee_update.html",context={"get.Employee":getEmployee})

def Employee_delete(request,id):
    getEmployee=Employee_Table.objects.get(id=id)
    if (request.method=="POST"):
        data=request.POST
        getEmployee.delete()
        return redirect("/Employee_View")
    return render(request,"Employee_delete.html",context={"get.Employee":getEmployee})    

