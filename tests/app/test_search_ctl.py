import pytest

from search_ctl import SearchApp
from models import OrganizationDAO, UserDAO


@pytest.fixture
def app():
  return SearchApp()

def test_ctl_init(app):
  assert type(app.org_dao) is OrganizationDAO
  assert type(app.user_dao) is UserDAO

def test_ctl_load(app):
  app.load_data()
  assert isinstance(app.org_dao, OrganizationDAO)
  assert isinstance(app.user_dao, UserDAO)

def test_ctl_org_by_id(app):
  app.load_data()
  org_result = app.search_organisations("_id", 102)
  assert org_result.item['name'] == 'Nutralab'
  with pytest.raises(Exception):
    app.search_organisations("_id", 99)

def test_ctl_user_by_id(app):
  app.load_data()
  org_result = app.search_users("_id", 75)
  assert org_result.item['name'] == 'Catalina Simpson'
  with pytest.raises(Exception):
    app.search_users("_id", -1)