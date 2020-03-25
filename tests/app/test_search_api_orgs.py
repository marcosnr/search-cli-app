import pytest

from search_ctl import SearchAPI
from models import OrganizationDAO
from result_set import ResultSet, DefaultResultSet


@pytest.fixture
def search_data():
  test_org_data =	 [
    {
      "_id": 101,
      "url": "http://initech.zendesk.com/api/v2/organizations/101.json",
      "external_id": "9270ed79-35eb-4a38-a46f-35725197ea8d",
      "name": "Enthaze",
      "domain_names": [
        "kage.com",
        "ecratic.com",
        "endipin.com",
        "zentix.com"
      ],
      "created_at": "2016-05-21T11:10:28 -10:00",
      "details": "",
      "shared_tickets": False,
      "tags": [
        "Fulton",
        "West",
        "Rodriguez",
        "Farley"
      ]
    }
  ]
  test_org_dao = OrganizationDAO()
  test_org_dao.organizations = test_org_data
  search_data.org_dao = test_org_dao
  return search_data

def test_search_org_by_id(search_data):
  org = SearchAPI.search_org_by_id(search_data.org_dao, 101)
  assert isinstance(org, dict)
  assert org['name'] == 'Enthaze'
  with pytest.raises(Exception):
    org_result = SearchAPI.search_org_by_id(search_data.org_dao, 102)

def test_search_org_by_field(search_data):
  org_result_set = SearchAPI.search_org_by_field(search_data.org_dao, "name", "Enthaze")
  assert isinstance(org_result_set, ResultSet)
  assert org_result_set.item['_id'] == 101

def test_search_org_by_non_existent_field(search_data):
  org_result_set = SearchAPI.search_org_by_field(search_data.org_dao, "name", "field_invalid")
  assert isinstance(org_result_set, DefaultResultSet)
  assert org_result_set.query_value == 'field_invalid'

def test_search_org_by_empty_value(search_data):
  org_result_set = SearchAPI.search_org_by_field(search_data.org_dao, "details", "")
  assert isinstance(org_result_set, ResultSet)
  assert org_result_set.item['name'] == 'Enthaze'

