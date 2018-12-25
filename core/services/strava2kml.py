import polyline

def activity2kml(name, summary, i):
    coords = polyline.decode(summary)
    colors = ['blueLine', 'redLine', 'greenLine', 
      'orangeLine', 'yellowLine', 'pinkLine', 
      'brownLine', 'purpleLine'
    ]
    return """
    <Placemark>
      <name>{name}</name>
      <visibility>0</visibility>
      <description>DESCRIPTION</description>
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
      name=name, 
      longitude=coords[0][1], 
      latitude=coords[0][0], 
      color=colors[i%len(colors)], 
      coordinates='\n                    '.join(['%s,%s,2357' % (lng,lat) for (lat, lng) in coords])
    )

def strava2kml(activities):
  return """
<?xml version="1.0" encoding="UTF-8"?>
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
</kml>
""" % '\n'.join([activity2kml(act['name'], act['map']['summary_polyline'], i) for i, act in enumerate(activities)])
