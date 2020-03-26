import pytest

from search_ctl import SearchApp
from models import OrganizationDAO, UserDAO, TicketDAO


@pytest.fixture
def app():
  return SearchApp()

@pytest.fixture
def app():
  return SearchApp()

def test_ctl_init(app):
  assert type(app.org_dao) is OrganizationDAO
  assert type(app.user_dao) is UserDAO
  assert type(app.ticket_dao) is TicketDAO

def test_ctl_load(app):
  app.load_data()
  assert isinstance(app.org_dao, OrganizationDAO)
  assert isinstance(app.user_dao, UserDAO)
  assert isinstance(app.ticket_dao, TicketDAO)

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

def test_ctl_ticket_by_id(app):
  app.load_data()
  org_result = app.search_tickets("_id", "436bf9b0-1147-4c0a-8439-6f79833bff5b")
  assert org_result.item['type'] == 'incident'
  with pytest.raises(Exception):
    app.search_tickets("_id", 100)