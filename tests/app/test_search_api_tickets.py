import pytest

from search_ctl import SearchAPI
from models import TicketDAO
from result_set import ResultSet, DefaultResultSet


@pytest.fixture
def search_data():
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
    },
    {
      "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
      "url": "http://initech.zendesk.com/api/v2/tickets/1a227508-9f39-427c-8f57-1b72f3fab87c.json",
      "external_id": "3e5ca820-cd1f-4a02-a18f-11b18e7bb49a",
      "created_at": "2016-04-14T08:32:31 -10:00",
      "type": "incident",
      "subject": "A Catastrophe in Micronesia",
      "description": "Aliquip excepteur fugiat ex minim ea aute eu labore. Sunt eiusmod esse eu non commodo est veniam consequat.",
      "priority": "low",
      "status": "hold",
      "submitter_id": 1,
      "assignee_id": 1,
      "organization_id": 101,
      "tags": [
        "Puerto Rico",
        "Idaho",
        "Oklahoma",
        "Louisiana"
      ],
      "has_incidents": False,
      "due_at": "2016-08-15T05:37:32 -10:00",
      "via": "chat"
    }
  ]
  test_ticket_dao = TicketDAO()
  test_ticket_dao.tickets = test_ticket_data
  search_data.ticket_dao = test_ticket_dao
  return search_data

def test_search_ticket_by_id(search_data):
  ticket = SearchAPI.search_ticket_by_id(search_data.ticket_dao, "436bf9b0-1147-4c0a-8439-6f79833bff5b")
  assert isinstance(ticket, dict)
  assert ticket['subject'] == 'A Catastrophe in Korea (North)'
  with pytest.raises(Exception):
    ticket_result = SearchAPI.search_ticket_by_id(search_data.ticket_dao, 99)

def test_search_ticket_by_field(search_data):
  ticket_result_set = SearchAPI.search_ticket_by_field(search_data.ticket_dao, 'external_id', '9210cdc9-4bee-485f-a078-35396cd74063')
  assert isinstance(ticket_result_set, ResultSet)
  assert ticket_result_set.item['_id'] == "436bf9b0-1147-4c0a-8439-6f79833bff5b"
