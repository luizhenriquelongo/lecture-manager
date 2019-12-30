import pytest
import requests
import sys
import json

sys.path.append('../')

from app import lecture_manager

def test_no_body_request():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=None
        )
    assert response.status_code == 400

def test_not_dict_body_request():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=json.dumps(['1', '2', '3']),
        headers={'Content-type': 'application/json'}
        )
    assert response.status_code == 400

def test_empty_body_request():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=json.dumps({"data": []}),
        headers={'Content-type': 'application/json'}
        )
    assert response.status_code == 400

def test_not_dict_data_request():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=json.dumps({"data": {'1':1, '2':2, '3':3}}),
        headers={'Content-type': 'application/json'}
        )
    assert response.status_code == 400

def test_incorrect_data_format():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=json.dumps({"data": ['this data shall not pass!']}),
        headers={'Content-type': 'application/json'}
        )
    assert response.status_code == 400

def test_enough_data():
    response = requests.post(
        url='http://127.0.0.1:5000/api/v1/lecture_manager',
        data=json.dumps({"data": [
            "Writing Fast Tests Against Enterprise Rails 15min",
            "Overdoing it in Python 45min"
        ]}),
        headers={'Content-type': 'application/json'}
        )
    assert response.status_code == 400

