import logging
import config

from result_set import DefaultResultSet, ResultSet

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class SearchAPI:
  """Search (proto)API for Organizations and Ticketing"""

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
            return ResultSet(org, field, search_value)
      elif value == search_value:
        return ResultSet(org, field, search_value)

    logging.info(f"could not MATCH: '{search_value}' with any field: '{field}'")
    return DefaultResultSet(field, search_value)
