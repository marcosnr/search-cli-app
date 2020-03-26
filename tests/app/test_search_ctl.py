import pytest

from search_ctl import SearchApp
from models import OrganizationDAO, UserDAO, TicketDAO


@pytest.fixture(scope="function")
def app_init():
  return SearchApp()

@pytest.fixture(scope="module")
def app():
  app = SearchApp()
  app.load_data()
  return app

def test_ctl_init(app_init):
  assert type(app_init.org_dao) is OrganizationDAO
  assert type(app_init.user_dao) is UserDAO
  assert type(app_init.ticket_dao) is TicketDAO

def test_ctl_load(app):
  assert isinstance(app.org_dao, OrganizationDAO)
  assert isinstance(app.user_dao, UserDAO)
  assert isinstance(app.ticket_dao, TicketDAO)

def test_ctl_org_by_id(app):
  org_result = app.search_organisations("_id", 101)
  assert org_result.item['name'] == 'Enthaze'
  with pytest.raises(Exception):
    app.search_organisations("_id", 99)

def test_ctl_user_by_id(app):
  org_result = app.search_users("_id", 1)
  assert org_result.item['name'] == 'Francisca Rasmussen'
  with pytest.raises(Exception):
    app.search_users("_id", -1)

def test_ctl_ticket_by_id(app):
  org_result = app.search_tickets("_id", "436bf9b0-1147-4c0a-8439-6f79833bff5b")
  assert org_result.item['type'] == 'incident'
  with pytest.raises(Exception):
    app.search_tickets("_id", 100)