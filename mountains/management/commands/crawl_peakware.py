# coding: utf-8
from django.core.management.base import BaseCommand
from pyquery import PyQuery as pq
from mountains.models import Mountain
from django.contrib.gis.geos import Point


def parse_value_if_exists(key, mountain):
    return '%s: %s\n' % (key, mountain.get(key)) if mountain.get(key) else ''


def curiosities(mountain):
    return "%s%s%s%s%s%s%s" % (
      'First ascent on %s by %s\n' % (
          mountain.get('Year first climbed'), mountain.get('First successful climber(s)')
      ) if mountain.get('Year first climbed') or mountain.get('First successful climber(s)') else '',
      parse_value_if_exists('Nearest major airport', mountain),
      parse_value_if_exists('description', mountain),
      parse_value_if_exists('Best months for climbing', mountain),
      parse_value_if_exists('Most recent eruption', mountain),
      parse_value_if_exists('Convenient Center', mountain),
      parse_value_if_exists('Volcanic status', mountain),
    )


def transform(mountain):
    return {
        'spot': Point(float(mountain['Latitude']), float(mountain['Longitude'])),
        'curiosities': curiosities(mountain),
        'province': mountain.get('Province'),
        'difficulty': mountain.get('Difficulty'),
        'elevation': int(
          float(mountain['Elevation (meters)'].replace(',', ''))
        ) if mountain.get('Elevation (meters)') else 0,
        'name': mountain['name'],
        'country': mountain.get('Country'),
        'state': mountain.get('State'),
        'region': mountain.get('Range/Region'),
    }


class Command(BaseCommand):
    help = "Populate Mountain DB with Peakware Data"

    def add_arguments(self, parser):
        parser.add_argument('--start')
        parser.add_argument('--stop')

    def handle(self, *args, **options):
        for i in range(int(options['start']), int(options['stop'])):
            print("crawling %i" % i)
            q = pq(url='https://www.peakware.com/peaks.php?pk=%i' % (i))
            mountain = {'id': i}
            trs = q('#overview table tr')
            print(len(trs))
            if len(trs):
                for tr in trs:
                    try:
                        print(str(tr))
                        key = pq(tr)('th').text().replace(' \n ', ' ').replace('\n', '').replace(':', '').strip()
                        value = pq(tr)('td').text().replace(' \n ', ' ').replace('\n', '')
                        print(key, value)
                        mountain[key] = value
                    except UnicodeDecodeError:
                        print('error unicode on mountain %i %s' % (i, key))
                try:
                    mountain['name'] = q('h1').text()
                except UnicodeDecodeError:
                    print('error unicode on mountain %i NAME' % i)
                try:
                    mountain['description'] = q('#peakDescription').text()
                except UnicodeDecodeError:
                    print('error unicode on mountain %i DESCRIPTION' % i)

                Mountain.objects.update_or_create(id=mountain['id'], defaults=transform(mountain))
