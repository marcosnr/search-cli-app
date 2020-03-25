import pytest

from search_ctl import SearchApp
from models import OrganizationDAO


@pytest.fixture
def app():
  return SearchApp()

def test_search_init(app):
  assert type(app.org_dao) is OrganizationDAO

def test_search_load(app):
  app.load_data()
  assert isinstance(app.org_dao, OrganizationDAO)

def test_search_org_by_id(app):
  app.load_data()
  org_result = app.search_organisations("_id", 102)
  assert org_result.item['name'] == 'Nutralab'
  with pytest.raises(Exception):
    app.search_organisations("_id", 99)
