import pytest

from search import SearchApp
from models import OrganizationDAO


@pytest.fixture
def app():
  return SearchApp()

def test_search_init(app):
  assert type(app.org_dao) is OrganizationDAO

def test_search_load(app):
  app.load_data()
  assert app.validate_data() is True

def test_search_org_by_id(app):
  app.load_data()
  org_result = app.search_organisations("_id", 102)
  assert org_result['name'] == 'Nutralab'
  with pytest.raises(Exception):
    app.search_organisations("_id", 99)
