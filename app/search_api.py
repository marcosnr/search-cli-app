import logging
import config

from result_set import DefaultResultSet, ResultSet

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class SearchAPI:
  """Search (proto)API for Organizations and Ticketing"""

# Organisations
  @staticmethod
  def search_org_by_id(org_dao, org_id):
    """Search an organization by its unique Id

    Keyword arguments:
    org_dao -- DAO to access organization data (OrganizationDAO)
    org_id -- unique id (Integer)
    """
    logging.debug(f"search_org_by_id: {org_id}")
    for org in org_dao.organizations:
      if str(org.get("_id")) == str(org_id):
        logging.info(f"{org_id} Found - {org.get('name')}")
        return org
    raise Exception(f"org_id: {org_id} not found in Datastore")

  @staticmethod
  def search_org_by_field(org_dao, field, search_value):
    """Search an organization by any field

    Keyword arguments:
    org_dao -- DAO to access organization data (OrganizationDAO)
    field -- key field to search (String)
    search_value -- search value (String)
    """
    logging.debug(f"'{field}' -> '{search_value}'?")
    if field == "_id":
      org = SearchAPI.search_org_by_id(org_dao, search_value)
      return ResultSet(org, '_id', search_value)
    result = None
    for org in org_dao.organizations:
      value = org.get(field)
      if value is None:
        # Assuming schema is flexible, so checking each org...
        continue
      elif isinstance(value, list):
        # search inside list, e.g. 'tags'
        logging.debug(f"{field} is of list type")
        for iter in value:
          if iter == search_value:
            result = org
      elif value == search_value:
        result = org
      elif isinstance(value, bool):
        logging.debug(f"{value} is same bool equivalent as {search_value}?")
        if str(value) == search_value:
          logging.debug(f"yes it is")
          result = org
      if result is not None:
        return ResultSet(org, field, search_value)

    logging.info(f"could not MATCH: '{search_value}' with any field: '{field}'")
    return DefaultResultSet(field, search_value)

# Users
  @staticmethod
  def search_user_by_id(user_dao, user_id):
    """Search an users by its unique Id

    Keyword arguments:
    user_dao -- DAO to access users data (UserDAO)
    user_id -- unique id (Integer)
    """
    logging.debug(f"search_user_by_id: {user_id}")
    for user in user_dao.users:
      if str(user.get("_id")) == str(user_id):
        logging.info(f"{user_id} Found - {user.get('name')}")
        return user
    raise Exception(f"user_id: {user_id} not found in Datastore")

  @staticmethod
  def search_user_by_field(user_dao, field, search_value):
    """Search an users by any field

    Keyword arguments:
    user_dao -- DAO to access users data (UserDAO)
    field -- key field to search (String)
    search_value -- search value (String)
    """
    logging.debug(f"'{field}' -> '{search_value}'?")
    if field == "_id":
      user = SearchAPI.search_user_by_id(user_dao, search_value)
      return ResultSet(user, '_id', search_value)
    result = None
    for user in user_dao.users:
      value = user.get(field)
      logging.debug(f"{value} being tested now...")
      if value is None:
        logging.debug(f"value is none, continuing...")
        # Assuming schema is flexible, so checking each user...
        continue
      elif isinstance(value, list):
        # search inside list, e.g. 'tags'
        logging.debug(f"{value} is of list type")
        for iter in value:
          if iter == search_value:
            result = user
      elif value == search_value:
        result = user
      elif isinstance(value, bool):
        logging.debug(f"{value} is same bool equivalent as {search_value}?")
        if str(value) == search_value:
          logging.debug(f"yes it is")
          result = user
      if result is not None:
        return ResultSet(user, field, search_value)

# Tickets
  @staticmethod
  def search_ticket_by_id(ticket_dao, ticket_id):
    """Search an tickets by its unique Id

    Keyword arguments:
    ticket_dao -- DAO to access tickets data (TicketDAO)
    ticket_id -- unique id (Integer)
    """
    logging.debug(f"search_ticket_by_id: {ticket_id}")
    for ticket in ticket_dao.tickets:
      if str(ticket.get("_id")) == str(ticket_id):
        logging.info(f"{ticket_id} Found - '{ticket.get('subject')}'")
        return ticket
    raise Exception(f"ticket_id: {ticket_id} not found in Datastore")

  @staticmethod
  def search_ticket_by_field(ticket_dao, field, search_value):
    """Search a tickets by any field

    Keyword arguments:
    ticket_dao -- DAO to access tickets data (TicketDAO)
    field -- key field to search (String)
    search_value -- search value (String)
    """
    logging.debug(f"'{field}' -> '{search_value}'?")
    if field == "_id":
      ticket = SearchAPI.search_ticket_by_id(ticket_dao, search_value)
      return ResultSet(ticket, '_id', search_value)
    result = None
    for ticket in ticket_dao.tickets:
      value = ticket.get(field)
      if value is None:
        # Assuming schema is flexible, so checking each ticket...
        continue
      elif isinstance(value, list):
        # search inside list, e.g. 'tags'
        logging.debug(f"{value} is of list type")
        for iter in value:
          if iter == search_value:
            result = ticket
      elif value == search_value:
        result = ticket
      elif isinstance(value, bool):
        logging.debug(f"{value} is same bool equivalent as {search_value}?")
        if str(value) == search_value:
          logging.debug(f"yes it is")
          result = ticket
      if result is not None:
        return ResultSet(ticket, field, search_value)
