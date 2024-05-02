from django.shortcuts import render 
from pytube import *
from django.http import HttpResponse
from django.http import HttpResponse
import requests
  
  
def youtube(request): 
    if request.method == 'POST': 
        link = request.POST['link'] 
        video = YouTube(link) 
        stream = video.streams.get_lowest_resolution() 
        
        # Get the URL of the video stream
        stream_url = stream.url
        
        # Fetch the video content and send it as a response
        response = requests.get(stream_url)
        
        # Create a Django HttpResponse with video content
        video_response = HttpResponse(response.content, content_type='video/mp4')
        
        # Set content disposition to attachment to force download
        video_response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        
        return video_response
    
    return render(request, 'youtube.html')