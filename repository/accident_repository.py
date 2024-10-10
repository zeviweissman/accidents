from database.connection import get_accidents_collection, get_beats_collection
from toolz import pipe, partial, get_in

accidents = get_accidents_collection()
beats = get_beats_collection()

def get_total_accidents_by_beat(beat):
    return pipe (beats.aggregate([{
        '$match': {
        'beat': beat
        }},
        {
            '$project': {
        '_id' : False, 'total_accidents': 1
            }
        }
    ]),
        list,
        partial(get_in,[0, 'total_accidents'])
    )


def get_total_accidents_by_beat_and_date(beat, date):
    return pipe (beats.aggregate([{
        '$match': {
        'beat': beat,
        }},
        {
            '$project': {
        '_id' : False, f'total_accidents_by_date.{date}': 1
            }
        }
    ]),
        list,
        partial(get_in, [0, 'total_accidents_by_date', date])

    )


def get_total_accidents_by_beat_and_week(beat, week_date):
    return pipe (beats.aggregate([{
        '$match': {
        'beat': beat,
        }},
        {
            '$project': {
        '_id' : False, f'total_accidents_by_week.{week_date}': 1
            }
        }
    ]),
        list,
        partial(get_in, [0, 'total_accidents_by_week', week_date])

    )

