from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')


def get_db_connection():
    return client['accidents-stats']

def get_day_collection():
    return get_db_connection()['days']

def get_week_collection():
    return get_db_connection()['weeks']

def get_month_collection():
    return get_db_connection()['month']

def get_accidents_collection():
    return get_db_connection()['accidents']

def get_beats_collection():
    return get_db_connection()['beats']