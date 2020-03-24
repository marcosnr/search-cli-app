import logging
import config
from data_loader import DataLoader
from models import OrganizationDAO

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
    logging.info(f"search_org_by_id: {org_id}")
    for org in org_dao.organizations:
      if org['_id'] == org_id:
        logging.debug(f"Found {org['name']}")
        return org
    else:
      raise Exception(f"search_org_by_id: {org_id} not found in Datastore")


###
# Search Controller
if __name__ == '__main__':
  """Search Controller"""
  logging.info("Search APP MVP")
  # load data
  org_dao = OrganizationDAO()
  org_dao.organizations = DataLoader._load_file('assets/organizations.json')
  # validate data
  logging.info(f"loaded '{org_dao}' organizations")
  # search simple
  org_result = SearchAPI.search_org_by_id(org_dao, 102)
  logging.info(f"found {org_result}")
