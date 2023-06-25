from django.shortcuts import render


def home_view(request):
    # Add your logic for the home view
    return render(request, 'home.html')
