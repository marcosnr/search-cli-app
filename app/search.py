import logging
import config
from data_loader import DataLoader
from data_exporter import DataExporter
from models import OrganizationDAO
from search_api import SearchAPI

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class SearchApp:
  """ Simple Search App Controller to offer basic queries capabilities
  to an organization, with its users and tickets
  """

  def __init__(self):
    """Init App with default data"""
    logging.debug("initialising app...")
    self.organizations_uri = config.DEFAULT_ORG_DATA
    self.org_dao = OrganizationDAO()

  def load_data(self):
    """Load data sources in memory"""
    logging.debug("loading data...")
    self.org_dao.organizations = DataLoader._load_file(self.organizations_uri)
    self.validate_data()

  def validate_data(self):
    """Business Model Validation"""
    # TODO Can be expanded to own module
    logging.info(f"loaded '{self.org_dao}' organizations")
    if int(f"{self.org_dao}") > 0:
      return True
    else:
      raise Exception("organization data wasn't loaded properly")

  def search_organisations(self, attribute_name, value):
    """Search organizations by all fields

    Keyword arguments:
    attribute_name -- name of field
    value -- value of field to search
    """

    logging.info(f"searching by: field='{attribute_name}',value='{value}'")
    if attribute_name == "_id":
      org_result = SearchAPI.search_org_by_id(self.org_dao, value)
    else:
      raise Exception("field/option for search not available")
    logging.debug(f"found: {org_result['name']}")
    logging.debug(f"items: {org_result}")
    return org_result

  def export(self, results, export_type):
    """Exports results

    Keyword arguments:
    results -- resource to export
    export_type -- export type format
    """
    logging.debug(f"export_results as: '{export_type}'")
    if export_type == 'json':
      DataExporter.pretty_print(results)
    elif export_type == 'yaml':
      DataExporter.yaml_print(results)
    elif export_type == 'file':
      DataExporter.json_out(results)
    else:
      raise Exception("Export format not supported")
