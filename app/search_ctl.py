import logging
import config
from validator import Validator
from search_api import SearchAPI
from result_set import ResultSet
from data_loader import DataLoader
from data_exporter import DataExporter
from models import OrganizationDAO, UserDAO

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
    self.users_uri = config.DEFAULT_USER_DATA
    self.user_dao = UserDAO()

  def load_data(self):
    """Load data sources in memory"""
    logging.debug("loading default json input files...")
    self.org_dao.organizations = DataLoader._load_file(self.organizations_uri)
    Validator.validate_org_data(self.org_dao)
    self.user_dao.users = DataLoader._load_file(self.users_uri)
    Validator.validate_user_data(self.user_dao)

  def search_organisations(self, key_name, value):
    """Search organizations by all fields

    Keyword arguments:
    key_name -- name of field
    value -- value of field to search
    """

    logging.info(f"searching by: field='{key_name}',value='{value}'")
    Validator.validate_input(key_name, value)
    return SearchAPI.search_org_by_field(self.org_dao, key_name, value)

  def search_users(self, key_name, value):
    """Search users by all fields

    Keyword arguments:
    key_name -- name of field
    value -- value of field to search
    """

    logging.info(f"searching by: field='{key_name}',value='{value}'")
    Validator.validate_input(key_name, value)
    return SearchAPI.search_user_by_field(self.user_dao, key_name, value)

  def export(self, results, export_format):
    """Exports results

    Keyword arguments:
    results -- resource to export
    export_format -- export type format
    """
    if isinstance(results, ResultSet):
      logging.debug(f"found: {results.item['name']}")
      logging.debug(f"items: {results.item}")
      logging.debug(f"format: '{export_format}' ")
      if export_format == 'json':
        DataExporter.pretty_print(results.item)
      elif export_format == 'yaml':
        DataExporter.yaml_print(results.item)
      elif export_format == 'file':
        DataExporter.json_out(results.item)
      else:
        raise Exception("Export format not supported")
    else:
      print(f"Oops! {results}, want to try again?")
