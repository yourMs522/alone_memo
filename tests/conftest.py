import pytest as pytest
from pymongo import MongoClient


import app as flask_app

test_database_name = 'spartatest'
client = MongoClient('localhost', 27017)
db = client.get_database(test_database_name)


@pytest.fixture
def app():
    test_app = flask_app.create_app(test_database_name)

    # 제네레이터 문법 (yield구문 까지만 실행하고 대기 , 이후 다시 호출할 떄 yield 구문 다음이 진행됨)
    yield test_app

    # 여기서 부터 모든 테스트가 완료되고 나서 실행됨
    client.drop_database(test_database_name)
    print('테스트 DB 제거 완료 ')

