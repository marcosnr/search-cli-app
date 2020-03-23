import logging
import config
from data_loader import DataLoader
from models import OrganizationDAO

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)

###
# Search Controller
if __name__ == '__main__':
  logging.info("Search APP MVP")
  # load data
  org_dao = OrganizationDAO()
  org_dao.organizations = DataLoader._load_file('assets/organizations.json')
  # check data
  logging.info(f"loaded '{org_dao}' organizations")
  for org in org_dao.organizations:
      logging.debug(f"{org['name']} [_id:{org['_id']}]")
