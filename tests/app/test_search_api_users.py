import pytest

from search_ctl import SearchAPI
from models import UserDAO
from result_set import ResultSet, DefaultResultSet


@pytest.fixture
def search_data():
  test_user_data =	 [
    {
        "_id": 2,
        "url": "http://initech.zendesk.com/api/v2/users/2.json",
        "external_id": "c9995ea4-ff72-46e0-ab77-dfe0ae1ef6c2",
        "name": "Cross Barlow",
        "alias": "Miss Joni",
        "created_at": "2016-06-23T10:31:39 -10:00",
        "active": True,
        "verified": True,
        "shared": False,
        "locale": "zh-CN",
        "timezone": "Armenia",
        "last_login_at": "2012-04-12T04:03:28 -10:00",
        "email": "jonibarlow@flotonic.com",
        "phone": "9575-552-585",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 106,
        "tags": [
          "Foxworth",
          "Woodlands",
          "Herlong",
          "Henrietta"
        ],
        "suspended": False,
        "role": "admin"
      },
      {
        "_id": 3,
        "url": "http://initech.zendesk.com/api/v2/users/3.json",
        "external_id": "85c599c1-ebab-474d-a4e6-32f1c06e8730",
        "name": "Ingrid Wagner",
        "alias": "Miss Buck",
        "created_at": "2016-07-28T05:29:25 -10:00",
        "active": False,
        "verified": False,
        "shared": False,
        "locale": "en-AU",
        "timezone": "Trinidad and Tobago",
        "last_login_at": "2013-02-07T05:53:38 -11:00",
        "email": "buckwagner@flotonic.com",
        "phone": "9365-482-943",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 104,
        "tags": [
          "Mulino",
          "Kenwood",
          "Wescosville",
          "Loyalhanna"
        ],
        "suspended": False,
        "role": "end-user"
      }
  ]
  test_user_dao = UserDAO()
  test_user_dao.users = test_user_data
  search_data.user_dao = test_user_dao
  return search_data

def test_search_user_by_id(search_data):
  user_result_set = SearchAPI.search_user_by_id(search_data.user_dao, 2)
  assert isinstance(user_result_set, ResultSet)
  assert user_result_set.item['name'] == 'Cross Barlow'
  with pytest.raises(Exception):
    user_result = SearchAPI.search_user_by_id(search_data.user_dao, 0)

def test_search_user_by_field(search_data):
  user_result_set = SearchAPI.search_user_by_field(search_data.user_dao, 'created_at', '2016-06-23T10:31:39 -10:00')
  assert isinstance(user_result_set, ResultSet)
  assert user_result_set.item['_id'] == 2

def test_search_user_by_list_field(search_data):
  user_result_set = SearchAPI.search_user_by_field(search_data.user_dao, 'tags', 'Henrietta')
  assert isinstance(user_result_set, ResultSet)
  assert user_result_set.item['email'] == 'jonibarlow@flotonic.com'

def test_search_user_by_bool_field(search_data):
  user_result_set = SearchAPI.search_user_by_field(search_data.user_dao, 'suspended', 'False')
  assert isinstance(user_result_set, ResultSet)
  assert user_result_set.item['email'] == 'jonibarlow@flotonic.com'
