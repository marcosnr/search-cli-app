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
    logging.debug(f"search_org_by_field: {field}->? {search_value}")
    for org in org_dao.organizations:
      value = org.get(field)
      if value == 'None':
        # Assuming schema is flexible, so checking each org...
        continue
      elif value == search_value:
        logging.debug(f"Found {org['name']}")
        return ResultSet(org, field, search_value)
    logging.info(f"could not MATCH: '{search_value}' with any field: '{field}'")
    return DefaultResultSet(field, search_value)
