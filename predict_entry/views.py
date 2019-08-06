from predict_entry.predict_try import *
#import predict_entry.try
from django.shortcuts import render
from predict_entry.models import Predict
from predict_entry.forms import predict_form
import pandas as pd
fin=[]

def index(request):
    #form=predict_form()
    if request.method =="GET":
        return render(request, 'predict_entry/predicting_parameter.html')
    elif request.method=="POST":
        del fin[:]
        internet_service=request.POST['internet_service']
        print(internet_service)
        fin.append(internet_service)
        tenure=request.POST['tenure']
        ten=int(tenure)
        print(tenure)
        fin.append(tenure)
        phone_service = request.POST['phone_service']
        print(phone_service)
        fin.append(phone_service)
        multiple_lines=request.POST['multiple_lines']
        print(multiple_lines)
        fin.append(multiple_lines)
        contract=request.POST['contract']
        print(contract)
        fin.append(contract)
        payment=request.POST['payment']
        print(payment)
        fin.append(payment)
        online_security=request.POST['online_security']
        print(online_security)
        fin.append(online_security)
        online_backup =request.POST['online_backup']
        print(online_backup)
        fin.append(online_backup)
        stream_tv=request.POST['stream_tv']
        print(stream_tv)
        fin.append(stream_tv)
        stream_mov=request.POST['stream_mov']
        print(stream_mov)
        fin.append(stream_mov)
        tech_support=request.POST['tech_support']
        print(tech_support)
        fin.append(tech_support)

        data = {"InternetService": internet_service,"tenure": ten,"PhoneService": phone_service,"MultipleLines": multiple_lines,
                "Contract": contract,"PaymentMethod": payment,"OnlineSecurity": online_security,"OnlineBackup": online_backup,
                "StreamingTV": stream_tv,"StreamingMovies": stream_mov,"TechSupport": tech_support}
        print(data)
            #inst = pd.Series(data)
        print(fin)
        prediction = predict({"InternetService": internet_service,"tenure": ten,"PhoneService": phone_service,"MultipleLines": multiple_lines,
                "Contract": contract,"PaymentMethod": payment,"OnlineSecurity": online_security,"OnlineBackup": online_backup,
                "StreamingTV": stream_tv,"StreamingMovies": stream_mov,"TechSupport": tech_support},tree)
        print(prediction)
        if prediction=="Yes":
            context = {
                'prediction': 'The customer is likely to churn'
            }
        else:
            context={
                'prediction':'The customer is likely to stay'
            }

        entry=Predict(internet_service=internet_service,tenure=tenure,phone_service=phone_service,multiple_lines=multiple_lines,
                      contract=contract,payment=payment,online_security=online_security,online_backup=online_backup,stream_tv=stream_tv,
                      stream_mov=stream_mov,tech_support=tech_support)
        entry.save()
            #result=predictdata(request)
            #return result

            #print(prediction)
        return render(request,'predict_entry/output_parameter.html',context) #,{'success':True})
        #except Exception as e:
            #print("error in request")
            #return render(request, 'predict_entry/predicting_parameter.html',{'success': False})


'''
def predictdata(request):
    inp = fin
    #inp = [i for i in inp]
    #X_test = np.array([inp])
    val = predict(inp,tree)
    dictio = {'fin':val}
    return render(request,'predict_entry/output_parameter.html',context=dictio)

def index(request):
    data={"tenure":'8',"InternetService":"DSL","MultipleLines":"Yes","Contract":"Month-to-month","PaymentMethod":"Electronic check",
      "PhoneService":"No","OnlineSecurity":"No internet service","OnlineBackup":"No internet service","StreamingTV":"Yes",
      "StreamingMovies":"No","TechSupport":"No"}
    inst = pd.Series(data)
    print(inst)
    prediction = predict(data, tree)
    print(prediction)
    return render(request, 'predict_entry/output_parameter.html', {'prediction': [prediction]})
    

fin=[]
def index(request):
    form = predict_form()
    del fin[:]
   if request.method =="POST":
        form = predict_form(request.POST)
        data = request.POST
        internet_service = data('internet_service')
        print(internet_service)
        fin.append(internet_service)
        contract = data('contract')
        print(contract)
        fin.append(contract)
        payment = data('payment')
        print(payment)
        fin.append(payment)
        if form.is_valid():
            form.save(commit=True)
            return gre_predict(request)
        else:
            print("Form validation Failed")
    return render(request,"predict_entry/predict_form.html",{'form':form})


def gre_predict(request):
    inp = fin
    inp = [i for i in inp]
    X_test = np.array([inp])
    val = predict(inp,tree)
    dictio = {'fin':val}
    return render(request,'predict_entry/output_parameter.html',context=dictio)
'''