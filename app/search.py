import logging
import config
from data_loader import DataLoader
from models import OrganizationDAO
from search_api import SearchAPI

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class SearchApp:
  """ Simple Data Access Object Pattern implementation
  to support Accessing Organization type entities
  """

  def __init__(self):
    """Init App with default data"""
    logging.info("initialising app...")
    self.organizations_uri = 'assets/organizations.json'
    self.org_dao = OrganizationDAO()

  def validate_data(self):
    """Business Model Validation"""
    # TODO Can be expanded to own module
    logging.info(f"loaded '{self.org_dao}' organizations")
    if int(f"{self.org_dao}") > 0:
      return True
    else:
      raise Exception("organization data wasn't loaded properly")


  def load_data(self):
    """Load data sources in memory"""
    logging.info("loading data...")
    self.org_dao.organizations = DataLoader._load_file(self.organizations_uri)
    self.validate_data()

  def search_organisations(self,attribute_name,value):
    """Search organizations by all fields"""
    if attribute_name == "_id":
      org_result = SearchAPI.search_org_by_id(self.org_dao, value)
    # TODO else: if: etc... as we add functionality
    logging.info(f"found: {org_result['name']}")
    logging.debug(f"items: {org_result}")
    return org_result

# Entry Point
if __name__ == '__main__':
  """SearchApp Controller"""
  logging.info("Search Organizations APP MVP")
  # initialises app...
  app = SearchApp()
  # load defaults...
  app.load_data()
  # search simple example...
  attribute_name="_id"
  value=102
  app.search_organisations(attribute_name, value)
