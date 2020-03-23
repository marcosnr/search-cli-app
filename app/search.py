import json
import logging
import config
from data_loader import DataLoader

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)

###
# Search Controller
if __name__ == '__main__':
  logging.info("Search Controller!")
  organisations_dict = DataLoader._load_file('assets/organizations.json')
  for org in organisations_dict:
      print(org['name'])
  # orgs = OrganizationDAO()
  # orgs.set_organizations(organisations_dict)