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


