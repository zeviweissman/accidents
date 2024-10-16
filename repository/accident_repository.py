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


def get_accident_info_by_beat_grouped_by_primary_cause(beat):
    return list(accidents.aggregate([
        {
            '$match': {
                'beat': beat
            }
        },
        {
            '$group': {
                '_id': '$primary_contributory_cause',
                'count': {
                    '$sum': 1
                },
                'total_injuries': {
                    '$sum': '$total_injuries'
                },
                'total_fatal_injuries':{
                    '$sum': '$fatal_injuries'
                    }
            }
        },
        {
            '$project': {
                'cause': '$_id',
                '_id': False,
                'total_fatal_injuries': 1,
                'total_injuries': 1
            }
        }
    ]))



def get_stats_about_injuries_by_beat(beat):
    return list(accidents.aggregate([
        {
            '$match': {
                'beat': beat
            }
        },
        {
            '$group': {
                '_id': '$beat',
                'count': {
                    '$sum': 1
                },
                'total_non_fatal_injuries': {
                    '$sum': '$non_fatal_injuries'
                },
                'total_fatal_injuries': {
                    '$sum': '$fatal_injuries'
                },
                'accidents': {
                    '$push':{
                        'primary_contributory_cause': '$primary_contributory_cause' ,
                        'beat': "$beat",
                        'total_injuries': "$total_injuries",
                        'fatal_injuries': '$fatal_injuries',
                        'non_fatal_injuries': '$non_fatal_injuries',
                        'incapacitating_injuries': "$incapacitating_injuries",
                        'non_incapacitating_injuries': "$non_incapacitating_injuries",
                        'crash_date': "$crash_date"
                }
                }
            }
        },
        {
            '$project': {
                '_id': False,
                'beat': '$_id',
                'total_fatal_injuries': 1,
                'total_non_fatal_injuries': 1,
                'accidents': 1
            }
        }
    ]))


