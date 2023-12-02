from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'Main/index.html')

def MagicNumber(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        random_number = random.randint(0, 5)
        if number == random_number:
            return render(request, 'Main/MagicNumber.html', {'result': 'Ты угадал!'})
        else:
            return render(request, 'Main/MagicNumber.html', {'result': 'Ты не угадал :('})
    else: 
        return render(request, 'Main/MagicNumber.html')



