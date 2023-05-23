

from django.shortcuts import render


def demo(request):
   name="my dear students"
   return render(request,"index.html")
#def operations(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
  #  answer  = x + y
  #  answer1 = x - y
  #  answer2 = x * y
   # answer3 = x / y



  #  return render(request,"result.html",{'result':answer,'result1':answer1,'result2':answer2,'result3':answer3})

