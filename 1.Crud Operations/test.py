from app import app
import json


def test_registration():
    client = app.test_client()
    response = client.get('/')
    print(response)
    assert response.status_code == 200
    html = response.data.decode()
    assert 'Register' in html
    assert 'name="firstname"' in html
    assert 'name="lastname"' in html
    assert 'name="email"' in html
    assert 'name="gender"' in html
    assert 'name="hobbies"' in html
    assert 'name="country"' in html
    assert client.get("/").data == response.data
def test_show_details():
    client = app.test_client()
    response = client.get('/details')
    assert response.status_code == 200
def test_edit_details():
    client = app.test_client()
    response = client.get('/edit/3')
    assert response.status_code == 200
def test_update_details():
    client = app.test_client()
    response = client.post('/update/3',data={
        "firstname": "",
        "lastname": "",
        "email":"",
        "password":"",
        "gender":"",
        "hobbies":"",
        "country":""
        }
    )
    assert response.status_code == 302
def test_delete_details():
    client = app.test_client()
    response = client.post('/delete/1')
    assert response.status_code == 302
"""
import unittest
#import requests
from app import app

class TestApp(unittest.TestCase):

    def test_registration(self):
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        html = response.data.decode()
        assert 'name="firstname"' and 'name="lastname"' and 'name="email"' and  'name="gender"' and 'name="hobbies"' and 'name="country"' in html
        """
        assert 'Register' in html
        assert 'name="firstname"' in html
        assert 'name="lastname"' in html
        assert 'name="email"' in html
        assert 'name="gender"' in html
        assert 'name="hobbies"' in html
        assert 'name="country"' in html
        """
        assert client.get("/").data == response.data
    def test_registration_validation(self):
        client = app.test_client()
        response = client.post('/create',data={
            "firstname": "",
            "lastname": "",
            "email":"",
            "password":"",
            "gender":"",
            "hobbies":"",
            "country":""
            })
        assert response.status_code == 200
        html = response.data.decode()
        #print(html)
        assert 'Please fill all the details' or 'Invalid email address!' or 'user already exists!' or 'Password should be combination of alphabets, special characters, digits and length of password is greater than 8'in html
        
    def test_show_details(self):
        client = app.test_client()
        response = client.get('/details')
        html=response.data.decode()
        print(html)
        assert response.status_code == 200
    def test_edit_details(self):
        client = app.test_client()
        response = client.get('/edit/24')
        assert response.status_code == 200
    def test_update_details(self):
        client = app.test_client()
        response =client.post('/update/2',data={
            "firstname": "hi",
            "lastname": "hi",
            "email":"hi@gmail.com",
            "password":"Hi123@gmail.com",
            "gender":"male",
            "hobbies":"movies",
            "country":"usa"
            }
        )
        print(response)
        assert response.status_code == 302
    def test_delete_details(self):
        client = app.test_client()
        response = client.post('/delete/1')
        print(response)
        assert response.status_code == 302
        

#unittest.main()
"""
from app import app
import json


def test_registration():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode()
    assert 'Register' in html
    assert 'name="firstname"' in html
    assert 'name="lastname"' in html
    assert 'name="email"' in html
    assert 'name="gender"' in html
    assert 'name="hobbies"' in html
    assert 'name="country"' in html
    assert client.get("/").data == response.data
def test_show_details():
    client = app.test_client()
    response = client.get('/details')
    assert response.status_code == 200
def test_edit_details():
    client = app.test_client()
    response = client.get('/edit/3')
    assert response.status_code == 200
def test_update_details():
    client = app.test_client()
    response = client.post('/update/3',data={
        "firstname": "",
        "lastname": "",
        "email":"",
        "password":"",
        "gender":"",
        "hobbies":"",
        "country":""
        }
    )
    assert response.status_code == 302
def test_delete_details():
    client = app.test_client()
    response = client.post('/delete/1')
    assert response.status_code == 302
"""
"""
