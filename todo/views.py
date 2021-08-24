from django.shortcuts import render

# Create your views here.
# take a http request from the user
# return response to the user


def get_todo_list(request):
    return render(request, 'todo/todo_list.html')