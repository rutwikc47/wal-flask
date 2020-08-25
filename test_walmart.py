import pytest
import manage

@pytest.fixture
def app():
    app = manage.application
    app.debug = True
    return app.test_client()


# Test if the app is running correctly after the changes
def test_app(app):
    res = app.get("/")
    assert res.status_code == 200
