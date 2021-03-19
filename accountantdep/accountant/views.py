from django.shortcuts import render

def accountant_view(request):
    context = {}
    return render(request, 'accountant/accountant.html', context)
