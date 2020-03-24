import logging
import config
from data_loader import DataLoader
from models import OrganizationDAO
from search_api import SearchAPI

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)

if __name__ == '__main__':
  """SearchAPP Controller"""
  logging.info("Search Organizations APP MVP")
  # load data
  org_dao = OrganizationDAO()
  org_dao.organizations = DataLoader._load_file('assets/organizations.json')
  # validate data
  logging.info(f"loaded '{org_dao}' organizations")
  # search simple
  org_result = SearchAPI.search_org_by_id(org_dao, 102)
  logging.info(f"found {org_result}")
