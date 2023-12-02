from django.shortcuts import render
from .models import Video


# Create your views here.
def play_list(request):
    video = Video.objects.all()
    return render(request, 'PlayList/PlayList.html', {'videos': video})

def create_video(request):
    print(request.POST)
    if request.method == 'POST':
        embed_code = request.POST['embed_code']
        name = request.POST['name']
        Video.objects.create(
            name=name,
            embed_code=embed_code
        )
    return render(request, 'PlayList/create_video.html')