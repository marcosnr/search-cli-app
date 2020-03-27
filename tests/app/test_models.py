import pytest

from models import OrganizationDAO, UserDAO, TicketDAO


@pytest.fixture
def org_dao():
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
  return test_org_dao

@pytest.fixture
def user_dao():
  test_user_data =	 [
    {
      "_id": 18,
      "url": "http://initech.zendesk.com/api/v2/users/1.json",
      "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
      "name": "Francisca Rasmussen",
      "alias": "Miss Coffey",
      "created_at": "2016-04-15T05:19:46 -10:00",
      "active": True,
      "verified": True,
      "shared": False,
      "locale": "en-AU",
      "timezone": "Sri Lanka",
      "last_login_at": "2013-08-04T01:03:27 -10:00",
      "email": "coffeyrasmussen@flotonic.com",
      "phone": "8335-422-718",
      "signature": "Don't Worry Be Happy!",
      "organization_id": 119,
      "tags": [
        "Springville",
        "Sutton",
        "Hartsville/Hartley",
        "Diaperville"
      ],
      "suspended": True,
      "role": "admin"
    }
  ]
  test_user_dao = UserDAO()
  test_user_dao.users = test_user_data
  return test_user_dao

@pytest.fixture
def ticket_dao():
  test_ticket_data =	 [
    {
      "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
      "url": "http://initech.zendesk.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json",
      "external_id": "9210cdc9-4bee-485f-a078-35396cd74063",
      "created_at": "2016-04-28T11:19:34 -10:00",
      "type": "incident",
      "subject": "A Catastrophe in Korea (North)",
      "description": "Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.",
      "priority": "high",
      "status": "pending",
      "submitter_id": 75,
      "assignee_id": 1,
      "organization_id": 101,
      "tags": [
        "Ohio",
        "Pennsylvania",
        "American Samoa",
        "Northern Mariana Islands"
      ],
      "has_incidents": False,
      "due_at": "2016-07-31T02:37:50 -10:00",
      "via": "web"
    }
  ]
  test_ticket_dao = TicketDAO()
  test_ticket_dao.tickets = test_ticket_data
  return test_ticket_dao

# orgs
def test_organization_dao_size(org_dao):
  assert f"{org_dao}" == '1'

def test_organization_structure(org_dao):
  assert org_dao.organizations[0]['_id'] == 101

# users
def test_user_dao_size(user_dao):
  assert f"{user_dao}" == '1'

def test_user_structure(user_dao):
  assert user_dao.users[0]['_id'] == 18

# tickets
def test_ticket_dao_size(ticket_dao):
  assert f"{ticket_dao}" == '1'

def test_ticket_structure(ticket_dao):
  assert ticket_dao.tickets[0]['_id'] == '436bf9b0-1147-4c0a-8439-6f79833bff5b'

