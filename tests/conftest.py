import os
import sys
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
os.environ["FLASK_APP"] = "server.py"

from datetime import datetime
from app.routes import app
from app.models import Unit, History
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def runner():
    return app.test_cli_runner()

@pytest.fixture(scope='module')
def newUnit():
    new_unit = Unit(
        uuid="3fa85f64-5717-4562-b3fc-2c963f66a333",
        name="CATEGORY",
        updateTime=datetime.fromisoformat("2022-05-28T21:12:01.000"),
        ntype=1,
        parentId="3fa85f64-5717-4562-b3fc-2c963f66a332",
        price=100
    )
    return new_unit

@pytest.fixture(scope='module')
def newHistory():
    new_history = History(
        uuid="3fa85f64-5717-4562-b3fc-2c963f66a333",
        updateTime=datetime.fromisoformat("2022-05-28T21:12:01.000"),
        price=100
    )
    return new_history