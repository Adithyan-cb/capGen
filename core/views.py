from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    """Renders the main landing page with the upload zone."""
    return render(request, 'core/index.html')

@csrf_exempt
def generate(request):
    if request.method == 'POST':
        # To be replaced with LLM logic
        mock_captions = [
            "Chasing horizons and capturing the editorial essence of the moment. ✨",
            "Defined by precision, inspired by the canvas. A new narrative begins.",
            "Minimalist visuals meet maximalist stories. #capGen"
        ]
        
        mock_hashtags = [
            {'tag': '#editorial', 'popularity': 'low'},
            {'tag': '#aesthetic', 'popularity': 'medium'},
            {'tag': '#storytelling', 'popularity': 'high'},
            {'tag': '#minimalism', 'popularity': 'low'},
            {'tag': '#creativity', 'popularity': 'trending'},
            {'tag': '#visuals', 'popularity': 'medium'},
            {'tag': '#artofvisuals', 'popularity': 'high'}
        ]
        
        context = {
            'captions': mock_captions,
            'hashtags': mock_hashtags,
            'image_url': None, # Will be set once upload logic is implemented
        }
        return render(request, 'core/results.html', context)
    
    return redirect('home')
