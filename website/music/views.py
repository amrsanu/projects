from django.http import HttpResponse
from django.http import Http404
from .models import Album, Song
from django.template import loader
from django.shortcuts import render, get_object_or_404
#   can use render shortcut to directly return the HttpResponse.
#   In place of loader we can use render\



def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {'all_albums' : all_albums}
    return HttpResponse(template.render(context, request))
#   in place of httpresponse, and remove the template variable
#   both the lines combined work as render below.
##  return render(request, 'music/index.html', context)




def detail(request, album_id):
#    try:
#        album = Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404("Album Does not exist !!!")
###   In palce of all the try except block we can simply use <get_object_or_404()>
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})

def favorite(request, albumm_id):
    album = get_object_or_404(Album, pk=albumm_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "you did not selected a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})