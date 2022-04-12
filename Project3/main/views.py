# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import requests
from isodate import parse_duration
from django.views.decorators.csrf import ensure_csrf_cookie

from re import U
from typing import overload

from .models import User
# Create your views here.

def home(request):
    return render(request, "main/home.html", {})

def diet(request):
    return render(request, "main/diet.html", {})

def quiz(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']

        eating = request.POST.get('eating')
        exercise = request.POST.get('exercise')
        habits = request.POST.get('habits')

        improve_answers = [eating, exercise, habits]

        diabetes = request.POST.get('diabetes') 
        cardiovascular = request.POST.get('cardiovascular')
        underweight = request.POST.get('underweight')
        overweight = request.POST.get('overweight')
        pre_existing_other = request.POST.get('pre-existing-other')

        preexisting_conditions = [diabetes, cardiovascular, underweight, overweight, pre_existing_other]

        vegetarian = request.POST.get('vegetarian')
        vegan = request.POST.get('vegan')
        gluten_free = request.POST.get('gluten-free')
        allergies = request.POST.get('allergies')
        pescatarian = request.POST.get('pescatarian')
        lactose_intolerant = request.POST.get('lactose-intolerant')
        dietary_other = request.POST.get('dietary-other')

        dietary_restrictions = [vegetarian, vegan, gluten_free, allergies, pescatarian, lactose_intolerant]

        high_intensity = request.POST.get('high-intensity')
        low_intensity = request.POST.get('low-intensity')
        cardio = request.POST.get('cardio')
        dance = request.POST.get('dance')
        strength_training = request.POST.get('strength-training')
        yoga = request.POST.get('yoga')
        pilates = request.POST.get('pilates')

        workouts = [high_intensity, low_intensity, cardio, dance, strength_training, yoga, pilates]

        arms = request.POST.get('arms')
        chest = request.POST.get('chest')
        lower_leg = request.POST.get('lower-leg')
        upper_leg = request.POST.get('upper-leg')
        core = request.POST.get('core')
        full_body = request.POST.get('full-body')

        workout_body_area = [arms, chest, lower_leg, upper_leg, core, full_body]


        print(first_name)
        print(preexisting_conditions)

        user = User(first_name=first_name, last_name=last_name, improve_answer=improve_answers, preexisting_conditions=preexisting_conditions, dietary_restrictions=dietary_restrictions, workouts=workouts, workout_body_area=workout_body_area, workout_days_per_week=3, streak_count=3)
        user.save();

        return redirect('/')
    else:
        return render(request, "main/quiz.html", {})

@ensure_csrf_cookie
def exercise(request):
    videos = []
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }
        r = requests.get(search_url,params=search_params)    
        
        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)
            
    context = {
        'videos' : videos
    }
    return render(request, "main/exercise.html",context)
    #return render(request, "main/exercise.html", {})

def analyzeDiet(request):
	edamam_url = 'https://api.edamam.com/api/nutrition-data'
	app_id = 'af21b52e'
	app_key = 'ba552652424df50cb5a78ce3de182372'
	ingr = '10kg apple'
	request_url = edamam_url+'?app_id='+app_id+'&app_key='+app_key+'&ingr='+ingr

	r = requests.get(request_url)
	
	results = r.json()

	try: 
		nutrience = {
			'calories': float(results['calories']), 
			'fat': float(results['totalNutrients']['FAT']['quantity']), 
			'carbohydrate': float(results['totalNutrients']['CHOCDF']['quantity']), 
			'protein': float(results['totalNutrients']['PROCNT']['quantity']), 
			'cholesterol': float(results['totalNutrients']['CHOLE']['quantity']), 
			'vit_A': float(results['totalNutrients']['VITA_RAE']['quantity']) / 1000000, 
			'vit_C': float(results['totalNutrients']['VITC']['quantity']) / 1000000, 
			'calcium': float(results['totalNutrients']['CA']['quantity']) / 1000, 
			'iron': float(results['totalNutrients']['FE']['quantity']) / 1000, 
			'sodium': (float(results['totalNutrients']['NA']['quantity']) / 1000)
		}
		print(nutrience)
	except: 
		print("ERROR")
	
	#if request.method == 'POST':
	#	breakfast = request.POST.get('breakfast', None)
	#	print("BI",breakfast)

	#food_items = []
	#print("Hell-")
	#for result in results: 
	#	print("Hell-")
	#	print(result)
	#	food_items.append(result)

	return render(request, "main/analyze_diet.html", {})
