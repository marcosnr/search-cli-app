import logging
import config
from data_loader import DataLoader
from data_exporter import DataExporter
from models import OrganizationDAO
from search_api import SearchAPI
from validator import Validator

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
    logging.debug("loading default json input...")
    self.org_dao.organizations = DataLoader._load_file(self.organizations_uri)
    Validator.validate_data(self.org_dao)

  def search_organisations(self, key_name, value):
    """Search organizations by all fields

    Keyword arguments:
    key_name -- name of field
    value -- value of field to search
    """

    logging.info(f"searching by: field='{key_name}',value='{value}'")
    Validator.validate_input(key_name, value)
    org_result = SearchAPI.search_org_by_field(self.org_dao, key_name, value)
    logging.debug(f"found: {org_result.item['name']}")
    logging.debug(f"items: {org_result.item}")
    return org_result

  def export(self, results, export_format):
    """Exports results

    Keyword arguments:
    results -- resource to export
    export_format -- export type format
    """    
    logging.debug(f"format: '{export_format}' ")
    if export_format == 'json':
      DataExporter.pretty_print(results.item)
    elif export_format == 'yaml':
      DataExporter.yaml_print(results.item)
    elif export_format == 'file':
      DataExporter.json_out(results.item)
    else:
      raise Exception("Export format not supported")
