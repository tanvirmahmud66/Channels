from django.shortcuts import render
from .models import Group, Chat

# Create your views here.
def IndexView(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    chats = []
    if group is not None:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group.objects.create(name = group_name)
        group.save()
    return render(request, 'app/index.html', {'group_name':group_name, 'chats':chats})