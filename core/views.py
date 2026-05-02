from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .services.caption import analyze_image_and_generate_captions
from .services.music import search_songs
import base64

def home(request):
    """Renders the main landing page with the upload zone."""
    return render(request, 'core/index.html')

@csrf_exempt
def generate(request):
    if request.method == 'POST':
        vibe = request.POST.get('vibe', 'Aesthetic')
        count = request.POST.get('count', '3')
        image_file = request.FILES.get('image')

        # Error handling for missing image
        if not image_file:
            messages.error(request, "please upload an image")
            return render(request, 'core/index.html', {'error': "please upload an image"})

        try:
            # Generate captions and hashtags
            # Note: We read the file here, but since we need it again for base64 display,
            # we should seek back to 0 or better yet, encode it once.
            
            # For display purposes on results page
            image_file.seek(0)
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            image_data_uri = f"data:{image_file.content_type};base64,{image_base64}"
            
            # Seek back to 0 for the service to read
            image_file.seek(0)
            results = analyze_image_and_generate_captions(image_file, vibe, count)
            
            # Process song recommendations
            songs = []
            seen_songs = set()
            raw_songs = results.get('song_recommendations', [])
            
            for idx, song in enumerate(raw_songs):
                if len(songs) >= 3:
                    break
                song_key = f"{song.get('artist_name', '').lower()}-{song.get('song_name', '').lower()}"
                if song_key in seen_songs:
                    continue
                seen_songs.add(song_key)
                
                track_data = search_songs(song.get('artist_name', ''), song.get('song_name', ''))
                if track_data and track_data.get('preview'):
                    track_data['id'] = idx + 1
                    songs.append(track_data)
            
            context = {
                'captions': results['captions'],
                'hashtags': results['hashtags'],
                'image_url': image_data_uri,
                'songs': songs,
            }
            return render(request, 'core/results.html', context)
        except Exception as e:
            print(f"Error during generation view: {e}")
            messages.error(request, "An error occurred during generation. Please try again.")
            return redirect('home')
    
    return redirect('home')
