from django.shortcuts import render

# Create your views here.
def IndexView(request, group_name):
    return render(request, 'app/index.html', {'group_name':group_name})
