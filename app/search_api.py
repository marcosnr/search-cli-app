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
      if org['_id'] == int(org_id):
        logging.debug(f"Found {org['name']}")
        return ResultSet(org, '_id', org_id)
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
      return SearchAPI.search_org_by_id(org_dao, search_value)
    result=None
    for org in org_dao.organizations:
      value = org.get(field)
      if value == 'None':
        # Assuming schema is flexible, so checking each org...
        continue
      elif isinstance(value, list):
        # search inside list, e.g. 'tags'
        logging.debug(f"{field} is of list type")
        for iter in value:
          if iter == search_value:
            result=org
      elif value == search_value:
          result=org
      elif isinstance(value, bool):
            result=org
      if result!= None:
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
      if user['_id'] == int(user_id):
        logging.debug(f"Found {user['name']}")
        return ResultSet(user, '_id', user_id)
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
      return SearchAPI.search_user_by_id(user_dao, search_value)
    result=None
    for user in user_dao.users:
      value = user.get(field)
      if value == 'None':
        # Assuming schema is flexible, so checking each user...
        continue
      elif isinstance(value, list):
        # search inside list, e.g. 'tags'
        logging.debug(f"{field} is of list type")
        for iter in value:
          if iter == search_value:
            result=user
      elif value == search_value:
          result=user
      elif isinstance(value, bool):
            result=user
      if result!= None:
        return ResultSet(user, field, search_value)
