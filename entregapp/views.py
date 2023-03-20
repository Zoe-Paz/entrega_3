from django.shortcuts import render

# Create your views here.
def gen(request):
    return render(request, './entregapp/gen.html')

