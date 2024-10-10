import csv
from datetime import datetime, date
from database.connection import get_accidents_collection, get_beats_collection
import utils.csv_utils as u


ACCIDENTS_CSV_PATH = "C:\\Users\\1\\PycharmProjects\\crush-stats\\assets\\data.csv"



def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_accidents():
    accidents = get_accidents_collection()
    beats = get_beats_collection()
    accidents.drop()
    beats.drop()

    for row in read_csv(ACCIDENTS_CSV_PATH):
        beat = row['BEAT_OF_OCCURRENCE']
        primary_cause = row['PRIM_CONTRIBUTORY_CAUSE']
        total_injuries = int(row['INJURIES_TOTAL']) if row['INJURIES_TOTAL'].isdecimal() else 0
        fatal_injuries = int(row['INJURIES_FATAL']) if row['INJURIES_FATAL'].isdecimal() else 0
        incapacitating_injuries = int(row['INJURIES_INCAPACITATING']) if row['INJURIES_INCAPACITATING'].isdecimal() else 0
        non_incapacitating_injuries = int(row['INJURIES_NON_INCAPACITATING']) if row['INJURIES_NON_INCAPACITATING'].isdecimal() else 0
        crash_date = u.parse_date(row['CRASH_DATE'])

        accident = {
                    'primary_contributory_cause': primary_cause,
                    'beat': beat,
                    'total_injuries' : total_injuries,
                    'fatal_injuries' : fatal_injuries,
                    'non_fatal_injuries' : total_injuries - fatal_injuries,
                    'incapacitating_injuries': incapacitating_injuries,
                    'non_incapacitating_injuries': non_incapacitating_injuries,
                    'crash_date': crash_date
        }

        get_accidents_collection().insert_one(accident).inserted_id
        date = u.parse_to_date_only(accident['crash_date'])
        week_date = u.convert_date_to_week_range(date)
        if not beats.find_one({'beat': beat}):
            beats.insert_one(
                {'beat': beat, 'total_accidents_by_date': {date: 1},
                 'total_accidents_by_week': {week_date: 1},
                 'total_accidents': 1,
                 })
        else:
            beats.update_one(
                {'beat': beat},
                {'$inc' : {
                  f'total_accidents_by_date.{date}': 1,
                  f'total_accidents_by_week.{week_date}': 1,
                    'total_accidents': 1
                }})

