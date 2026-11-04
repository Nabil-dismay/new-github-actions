from app import app


def test_home_returns_greeting():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    message = response.get_json()['message']
    assert 'Hello from the OpenShift CI/CD sample' in message


def test_health_returns_healthy():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'
