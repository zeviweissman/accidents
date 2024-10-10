from repository.seed_repository import init_accidents
import repository.accident_repository as repos
from database.connection import get_accidents_collection



def test_db_seed():
     init_accidents()
     assert len(list(get_accidents_collection().find().limit(5))) == 5


def test_accidents_by_beat():
    res = repos.get_total_accidents_by_beat("1822")
    assert res == 123

def test_accidents_by_beat_and_date():
    res = repos.get_total_accidents_by_beat_and_date("1822", '12/12/2023')
    assert res == 4

def test_accidents_by_beat_and_week():
    res = repos.get_total_accidents_by_beat_and_week("1822", "12/11/2023")
    assert res == 4

def test_get_accident_info_by_beat_grouped_by_primary_cause():
    res = repos.get_accident_info_by_beat_grouped_by_primary_cause("1822")
    assert res

def test_get_stats_about_injuries_by_beat():
    res = repos.get_stats_about_injuries_by_beat('1822')
    assert res