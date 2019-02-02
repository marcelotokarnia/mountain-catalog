import polyline
from datetime import datetime
from django.contrib.auth.models import User
import requests

def elapsed_time(elapsed):
  hours = elapsed // 3600
  elapsed = elapsed % 3600
  minutes = elapsed // 60
  seconds = elapsed % 60
  time = ''
  if hours > 0:
    time += '%dh' % hours 
  if minutes > 0:
    time += '%dm' % minutes
  return '%s%ds' % (time, seconds)

def get_activity_description(activity):
  return """<div style="line-height: 10px;">📅 {startdate} ({elapsed}) <br></br><br></br>
  🏁 {distance} <br></br>
  🏅 {achievements}<br></br>
  ⛰️ {elevation} <br></br>
  ⌚ {speed_pace} <br></br></div>""".format(
    startdate=datetime.strptime(activity['start_date_local'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%M/%y'),
    elapsed=elapsed_time(activity['elapsed_time']),
    distance='%.2f km' % (activity['distance'] / 1000),
    achievements='%s' % activity['achievement_count'],
    elevation='%s m gain' % activity['total_elevation_gain'],
    speed_pace='%.2f km/h (%.2f min/km)' % (activity['average_speed'] * 3.6, 50 / 3 / activity['average_speed']),
  )

def activity2kml(activity, i):
    summary = activity['map']['summary_polyline']
    coords = polyline.decode(summary)
    colors = ['blueLine', 'redLine', 'greenLine', 
      'orangeLine', 'yellowLine', 'pinkLine', 
      'brownLine', 'purpleLine'
    ]
    return """    <Placemark id="{id}">
      <name>{name}</name>
      <visibility>0</visibility>
      <description>{description}</description>
      <LookAt>
        <longitude>{longitude}</longitude>
        <latitude>{latitude}</latitude>
        <altitude>0</altitude>
        <heading>-106.8161545998597</heading>
        <tilt>44.60763714063257</tilt>
        <range>2569.386744398339</range>
      </LookAt>
      <styleUrl>#{color}</styleUrl>
      <LineString>
        <tessellate>1</tessellate>
        <altitudeMode>absolute</altitudeMode>
        <coordinates>
            {coordinates}
        </coordinates>
      </LineString>
    </Placemark>""".format(
      id=activity['id'],
      name=activity['name'], 
      description=get_activity_description(activity),
      longitude=coords[0][1], 
      latitude=coords[0][0], 
      color=colors[i%len(colors)], 
      coordinates='\n                    '.join(['%s,%s,2357' % (lng,lat) for (lat, lng) in coords])
    )

def strava2kml(username):
  access_token = User.objects.get(username=username).profile.strava_auth_token
  r = requests.get('https://www.strava.com/api/v3/athlete/activities', headers={
    'Authorization': 'Bearer %s' % access_token,
  })
  activities = r.json()
  return """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <Style id="blueLine">
      <LineStyle>
        <color>ffff0000</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="redLine">
      <LineStyle>
        <color>ff0000ff</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="greenLine">
      <LineStyle>
        <color>ff009900</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="orangeLine">
      <LineStyle>
        <color>ff00ccff</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="pinkLine">
      <LineStyle>
        <color>ffff33ff</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="brownLine">
      <LineStyle>
        <color>ff66a1cc</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="purpleLine">
      <LineStyle>
        <color>ffcc00cc</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="yellowLine">
      <LineStyle>
        <color>ff61f2f2</color>
        <width>4</width>
      </LineStyle>
    </Style>
%s
  </Document>
</kml>""" % '\n'.join([activity2kml(act, i) for i, act in enumerate(activities)])
