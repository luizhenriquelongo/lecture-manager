import pytest
import sys
import re
from datetime import datetime, time, timedelta
sys.path.append('../')

# local import
from controller import lectures_ordered_by_duration, total_minutes, start_time, create_dict, generate_tracks


@pytest.fixture
def data():
    return [
        "Writing Fast Tests Against Enterprise Rails 60min",
        "Overdoing it in Python 45min",
        "Lua for the Masses 30min",
        "Ruby Errors from Mismatched Gem Versions 45min",
        "Common Ruby Errors 45min",
        "Rails for Python Developers lightning",
        "Communicating Over Distance 60min",
        "Accounting-Driven Development 45min",
        "Woah 30min",
        "Sit Down and Write 30min",
        "Pair Programming vs Noise 45min",
        "Rails Magic 60min",
        "Ruby on Rails: Why We Should Move On 60min",
        "Clojure Ate Scala (on my project) 45min",
        "Programming in the Boondocks of Seattle 30min",
        "Ruby vs. Clojure for Back-End Development 30min",
        "Ruby on Rails Legacy App Maintenance 60min",
        "A World Without HackerNews 30min",
        "User Interface CSS in Rails Apps 30min"
    ]

@pytest.fixture
def test_data():
    return {
        5: [1,2],
        15: [1,2,3,4,5],
        30: [1,2,3,4],
        60: [1,2,3]
    }

def test_lectures_ordered_by_duration(data):
    data.append('Not suposed to work because has no Time')
    with pytest.raises(Exception):
        lectures_ordered_by_duration(data)

def test_total_minutes(test_data):
    assert total_minutes(test_data) == 385

def test_start_time():
    assert start_time('11:00AM', 75) == '12:15PM'
