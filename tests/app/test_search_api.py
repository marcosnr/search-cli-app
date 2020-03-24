import pytest

from search import SearchAPI
from models import OrganizationDAO


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
      "details": "MegaCorp",
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
  #TODO expand later to Mocks / other daos
  return search_data

def test_search_org_by_id(search_data):
  org_result = SearchAPI.search_org_by_id(search_data.org_dao, 101)
  assert type(org_result) is dict
  with pytest.raises(Exception):
    org_result = SearchAPI.search_org_by_id(search_data.org_dao, 102)

