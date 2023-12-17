from django import forms

class Time(forms.Form):
    p1 = forms.TimeField(label="PC_TIME1" , required=False)
    p2 = forms.TimeField(label="PC_TIME2" , required =False)
    p3 = forms.DateField(label="Date(YYYY-MM-DD)")

class Date(forms.Form):
    # date = forms.TypedChoiceField(label= "Enter Number Of Days" ,coerce = str, choices=(("1" , "5") , ("2" , "10") , ("3" , "15") , ("4" ,"20")))
    days = forms.CharField(label = "Enter Number Of Days" , max_length=200)
# the values 1 , 2 ,3 ,4 in choices refers to the index of that choice , we need to compare form.cleaned_data() value which is a string with that index not with the value!!!!
class Select(forms.Form):
    d1 = forms.DateField(label="From_Date(YYYY-MM-DD)")
    d2 = forms.DateField(label="To_Date(YYYY-MM-DD)")
