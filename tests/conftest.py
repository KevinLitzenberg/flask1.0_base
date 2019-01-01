import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

# tempfile.mkstemp() creates a temp files object repesenting the db.
@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    # client fixture creates application object for TESTING
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

# client fixture calls app.test_client() with the app object created above.
@pytest.fixture
def client(app):
    return app.test_client()

# runner fixture creates a runner that can call the Click commands.
@pytest.fixture
def runner(app):
    return app.test_cli_runner()


# create a class with methods that make a POST request to the login view and use fixture to pass it to the client. 
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

# with the auth fixture call auth.login() in a test to login as test user, which is inserted as part of the test data in the app fixture.
@pytest.fixture
def auth(client):
    return AuthActions(client)
