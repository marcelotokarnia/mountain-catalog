from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
import requests
import json

def authenticate(request):
  json_body = json.loads(request.body.decode('utf-8'))
  code = json_body.get('code')
  r = requests.post('https://www.strava.com/oauth/token', data={
    'client_id': 28106,
    'client_secret': settings.STRAVA_CLIENT_SECRET,
    'code': code,
    'grant_type': 'authorization_code'
  })
  strava_content = r.json()
  print(strava_content)
  email = strava_content['athlete']['email']
  user = User.objects.filter(email=email).first()
  if not user:
    first_name = strava_content['athlete']['firstname']
    last_name = strava_content['athlete']['lastname']
    username = strava_content['athlete']['username']
    user = User(email=email, first_name=first_name, last_name=last_name, username=username)
    user.save()
  user.profile.strava_auth_token = strava_content['access_token']
  user.profile.strava_refresh_token = strava_content['refresh_token']
  user.profile.save()
  login(request, user)
  return HttpResponse(status=204)
