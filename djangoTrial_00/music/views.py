from django.shortcuts import render, get_object_or_404
from .models import Album, Song

from django.views import generic

# Generic view - classes
class IndexView(generic.ListView):
	template_name = 'music/index.html'
	
	def get_queryset(self):
		return Album.objects.all()
	

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
	

# Normal view - functions
def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

	
def detail(request, albumIDs):
	album = get_object_or_404(Album, pk=albumIDs)
	return render(request, 'music/detail.html', {'album': album})

	
def favorite(request, albumIDs):
	album = get_object_or_404(Album, pk=albumIDs)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': "You did not select a valid song"
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})
