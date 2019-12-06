from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv, re
from datetime import date

class Command(BaseCommand):
    help ='import squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='file path')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        with open(path, mode='r') as f:
            reader = csv.DictReader(f)
            data = set()
            for row in reader:
                if row.get('Unique Squirrel ID') in data:
                    continue
                else:
                    m,d,y = pattern.match(row.get('Date')).groups()
                    obj, created = Squirrel.objects.get_or_create(
                        X = row.get('X'),
                        Y = row.get('Y'),
                        Unique_Squirrel_ID = row.get('Unique Squirrel ID'),
                        Hectare = row.get('Hectare'),
                        Shift = row.get('Shift'),
                        Date = date(int(y),int(m),int(d)),
                        Hectare_Squirrel_Number = row.get('Hectare Squirrel Number'),
                        Age = row.get('Age'),
                        Primary_Fur_Color = row.get('Primary Fur Color'),
                        Highlight_Fur_Color = row.get('Highlight Fur Color'),
                        Combination_Fur = row.get('Combination of Primary and Highlight Color'),
                        Color_Notes = row.get('Color Notes'),
                        Location = row.get('Location'),
                        Specific_Location = row.get('Specific Location'),
                        Running = row.get('Running'),
                        Chasing = row.get('Chasing'),
                        Climbing = row.get('Climbing'),
                        Eating = row.get('Eating'),
                        Foraging = row.get('Foraging'),
                        Other_Activities = row.get('Other Activities'),
                        Kuks = row.get('Kuks'),
                        Quaas = row.get('Quaas'),
                        Moans = row.get('Moans'),
                        Tail_Flags = row.get('Tail flags'),
                        Tail_Twitches = row.get('Tail twitches'),
                        Approaches = row.get('Approaches'),
                        Indifferent = row.get('Indifferent'),
                        Runs_From = row.get('Runs from'),
                        Other_Interactions = row.get('Other Interactions'),
                        Lat_Long = row.get('Lat/Long'),
                        Zip_Codes = row.get('Zip Codes'),
                        Community_Districts = row.get('Community Districts'),
                        Borough_Boundaries = row.get('Borough Boundaries'),
                        City_Council_Districts = row.get('City Council Districts'),
                        Police_Precincts = row.get('Police Precincts'),
                     )
                data.add(row.get('Unique Squirrel ID'))
        print('Success!')