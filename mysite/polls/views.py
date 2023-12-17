from .models import New , N
from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader
from .forms import Time , Date , Select
from polls.data_insert import function , func
import sqlite3
import pandas as pd

def main(request):
  function()
  mydata = New.objects.all()
  template = loader.get_template('template.html')
  context = {
    'news': mydata,
  }
  return HttpResponse(template.render(context, request))
def main1(request):
  func()
  mydata = New.objects.all()
  template = loader.get_template('temp1.html')
  context = {
    'news': mydata,
  }
  return HttpResponse(template.render(context, request))

def table(request):
    import threading
    lock = threading.Lock()
    with lock:
        sql_connect = sqlite3.connect(r'.\\lite.sqlite3')
    if(request.method == "POST"):
            form = Time(request.POST)
            if form.is_valid():
              a = form.cleaned_data["p1"]
              b = form.cleaned_data["p2"]
              c = form.cleaned_data["p3"]
              # import json
              if a!=None and b!=None:
                query = "SELECT * FROM t WHERE date = :z AND pc_time BETWEEN :x AND :y"
              else:
                 query = "SELECT * FROM t WHERE date = :z"
              df = pd.read_sql_query(query,sql_connect , params={'x':str(object =a) , 'y':str(object =b) , 'z':str(object=c)})
              sql_connect.close() 
              col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay' , 'iserror' ]
              df1=df[col].fillna('')
              new_data = df1[col].to_dict('records')
              new_entries = [ ]
              mydata = N.objects.all()
              if mydata.count() !=0:
                mydata.delete()
              for d in new_data:
                new_obj = N(**d)
                new_entries.append(new_obj)
              N.objects.bulk_create(new_entries)
              return render(request ,"lastpage.html" ,{'n':mydata}) 
    form1 = Time()
    form2 = Date()
    form3 = Select()
    return render(request , "t.html" , {"form1":form1 , "form2":form2 , "form3":form3})

def first_page(request):
    function()
    mydata = New.objects.all()
    template = loader.get_template('first_page.html')
    context = {
    'news': mydata,
    }
    return HttpResponse(template.render(context, request))

def data(request):
    import threading
    lock = threading.Lock()
    with lock:
        sql_connect = sqlite3.connect(r'.\\lite.sqlite3')
    if(request.method == "POST"):
            form = Date(request.POST)
            if form.is_valid():
              a = form.cleaned_data["days"]
              # import json
              query = "SELECT * FROM t WHERE date > (SELECT date('now', '-" + str(a)+" day'))"
              df = pd.read_sql_query(query,sql_connect)
              sql_connect.close()
              # object = df.to_html()
              # return HttpResponse(object)
              col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay' , 'iserror' ]
              df1=df[col].fillna('')
              new_data = df1[col].to_dict('records')
              new_entries = [ ]
              mydata = N.objects.all()
              if mydata.count() !=0:
                mydata.delete()
              for d in new_data:
                new_obj = N(**d)
                new_entries.append(new_obj)
              N.objects.bulk_create(new_entries)
              return render(request ,"lastpage.html" ,{'n':mydata})
    form1 = Time()
    form2 = Date()
    form3 = Select()
    return render(request , "t.html" , {"form1":form1 , "form2":form2 , "form3":form3})
def form(request):
    import threading
    lock = threading.Lock()
    with lock:
        sql_connect = sqlite3.connect(r'.\\lite.sqlite3')
    if(request.method == "POST"):
            form = Select(request.POST)
            if form.is_valid():
              a1 = form.cleaned_data["d1"]
              a2 = form.cleaned_data["d2"]
              # import json
              query = "SELECT * FROM t WHERE date BETWEEN :x AND :y"       
              df = pd.read_sql_query(query,sql_connect , params={"x":a1 , "y":a2})
              sql_connect.close()
              # object = df.to_html()
              # return HttpResponse(object)
              col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay' , 'iserror']
              df1=df[col].fillna('')
              new_data = df1[col].to_dict('records')
              new_entries = [ ]
              mydata = N.objects.all()
              if mydata.count() !=0:
                mydata.delete()
              for d in new_data:
                new_obj = N(**d)
                new_entries.append(new_obj)
              N.objects.bulk_create(new_entries)
              return render(request ,"lastpage.html" ,{'n':mydata})
    form1 = Time()
    form2 = Date()
    form3 = Select()
    return render(request , "t.html" , {"form1":form1 , "form2":form2 , "form3":form3})   

 

