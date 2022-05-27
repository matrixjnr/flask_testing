# test out flask api
from app import app

def testEcho():
    c = app.test_client()

    response = c.get('echo')
    assert response.status_code == 200
