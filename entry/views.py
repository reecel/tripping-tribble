from django.shortcuts import render

def post_list(request):
    return render(request, 'entry/post_list.html', {})
