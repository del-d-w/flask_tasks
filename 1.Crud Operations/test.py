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
