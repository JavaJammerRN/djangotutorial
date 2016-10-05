from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

# Just showing here that you can pass some content as dictionary to view useing render. see personal/basci.html
def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me','nacefredhwan@gmail.com']})
