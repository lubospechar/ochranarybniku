from django.core.management.base import BaseCommand, CommandError
import csv
import datetime

from data.models import Parameter, PondMeasurement, FiedlerData
from ponds.models import Pond


class Command(BaseCommand):
    help = 'Načte csv z fielderovsky dat'

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            dest="path",
            required=True,
            help="cesta k souboru",
        )


        parser.add_argument(
            "--pond_id",
            dest="pond_id",
            required=True,
            help="ID rybníku",
        )

    def handle(self, *args, **options):
        csv_file = options['path']
        
        pond = Pond.objects.get(pk=options['pond_id'])
    
        
        fields = {
            'pH': Parameter.objects.get(pk=7),
            'Srážky': Parameter.objects.get(pk=8),
            'Vlhkost 2m': Parameter.objects.get(pk=10),
            'Teplota 2m': Parameter.objects.get(pk=9),
            'GR dopad': Parameter.objects.get(pk=11),
            'GR odraz': Parameter.objects.get(pk=15),
            'Rozp.kyslík': Parameter.objects.get(pk=2),
            'Tepl.kyslík': Parameter.objects.get(pk=13),
            'Teplota pH': Parameter.objects.get(pk=14),
        }
        
        fields_position = {
            'Datum': 0, 
        }
        
        with open(csv_file, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=';')
            row_counter = 0
            for row in datareader:
                row_counter += 1
                if row_counter < 3: # přeskoč řádky
                    continue
                
                if row_counter == 3: # na řádku 3 musí být Labels
                    label_counter = 0
                    for label in row:
                        label_counter += 1
                        if label_counter == 1:
            
                            if not label == 'Labels:':
                                print('csv soubor je rozbity')
                                return
                            else:
                                continue
                        
                        l = label.strip()
                        if l in fields:
                            fields_position[l] = label_counter - 1
                    continue
                            

                if row_counter == 4: # na řádku 4 musí být Units
                    unit_counter = 0
                    for unit in row:
                        unit_counter += 1
                        if unit_counter == 1:
                            if not unit == 'Units:':
                                print('csv soubor je rozbity')
                                return
                            else:
                                continue
                    continue
                
                
                for f in fields_position:
                    position = fields_position[f]
                    try:
                        raw_data = row[position].strip()
                    except IndexError: # rozbitá hodnota bude vynechána
                        continue
                    
                    if position == 0:
                        dt = datetime.datetime.strptime(raw_data, '%d.%m.%Y %H:%M:%S')
                        pond_mesurement = PondMeasurement()
                        pond_mesurement.datetime = dt
                        pond_mesurement.pond = pond
                        pond_mesurement.note_cs = 'fiedler'
                        pond_mesurement.save()
                        
                    else:
                        raw_data = row[position].strip()
                        if raw_data == 'E11':
                            print(f'chyba E11 pro {f}, {dt}')
                            continue

                        if raw_data == 'E10':
                            print(f'chyba E11 pro {f}, {dt}')
                            continue
                        
                        if raw_data == '':
                            print(f'prázdná buňka pro {f}, {dt}')
                            continue
                        
                        data = float(raw_data.replace(',','.'))
                        
                        new_data = FiedlerData()
                        new_data.parameter = fields[f]
                        new_data.measurement = pond_mesurement
                        new_data.value = data
                        new_data.save()
                        
                        print(dt, data, fields[f])
        
            
            
            
