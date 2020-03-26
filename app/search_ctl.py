import logging
import config
from validator import Validator
from search_api import SearchAPI
from result_set import ResultSet
from data_loader import DataLoader
from data_exporter import DataExporter
from models import OrganizationDAO, UserDAO, TicketDAO

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class SearchApp:
  """ Simple Search App Controller to offer basic queries capabilities
  to an organization, with its users and tickets
  """
# setup logic
  def __init__(self):
    """Init App with default data"""
    logging.debug("initialising app...")
    self.organizations_uri = config.DEFAULT_ORG_DATA
    self.org_dao = OrganizationDAO()

    self.users_uri = config.DEFAULT_USER_DATA
    self.user_dao = UserDAO()

    self.tickets_uri = config.DEFAULT_TICKET_DATA
    self.ticket_dao = TicketDAO()

  def load_data(self):
    """Load data sources in memory"""
    logging.debug("loading all default json input files...")
    self.org_dao.organizations = DataLoader._load_file(self.organizations_uri)
    Validator.validate_org_data(self.org_dao)

    self.user_dao.users = DataLoader._load_file(self.users_uri)
    Validator.validate_user_data(self.user_dao)
    self.link_users()

    self.ticket_dao.tickets = DataLoader._load_file(self.tickets_uri)
    Validator.validate_ticket_data(self.ticket_dao)
    self.link_tickets()

  def link_users(self):
    """Link users to their respective organizations"""
    logging.debug("linking users with organizations...")
    for user in self.user_dao.users:
      for org in self.org_dao.organizations:
        try:
          org = SearchAPI.search_org_by_id(self.org_dao, user.get("organization_id"))
          logging.debug(f"linking {user['name']} -> {org['name']}")
          org['users'].append(user)
        except Exception as e:
          logging.warning(f"{e}, can't link user id {user.get('_id')}")
          logging.warning(f"{user.get('_id')} has invalid organization_id")
          if config.FULL_RELATIONAL:
            self.user_dao.users.remove(user)
          continue

  def link_tickets(self):
    """Link tickets to their respective organizations and users"""
    logging.debug("linking tickets with organizations...")
    for ticket in self.ticket_dao.tickets:
      # link to orgs
      for org in self.org_dao.organizations:
        try:
          logging.debug(f"linking {ticket.get('_id')} -> {org['name']}")
          org = SearchAPI.search_org_by_id(self.org_dao, ticket.get("organization_id"))
          org['tickets'].append(ticket)
        except Exception as e:
          logging.warning(f"{e}, can't link ticket id {ticket['_id']}")
          logging.warning(f"{ticket['_id']} has invalid organization_id: {ticket.get('organization_id')}")
          if config.FULL_RELATIONAL:
            self.ticket_dao.tickets.remove(ticket)
          continue
      # link existing users
      for user in self.user_dao.users:
        # link submitters
        try:
          submitter_id = ticket.get("submitter_id")
          if submitter_id == 'None':
            logging.debug(f"tck_id: {ticket['_id']} doesn't have a submitter")          
          else:
            submitter = SearchAPI.search_user_by_id(self.user_dao, submitter_id)
            logging.debug(f"linking submitter tck_id: {ticket['_id']} -> user_id {user['_id']}")
            submitter['tickets_submitted'].append(ticket)
        except Exception as e:
          logging.warning(f"{e}, can't link submitter to ticket!")
          logging.warning(f"submitter_id: {submitter_id} can't be found among registered users")
          if config.FULL_RELATIONAL:
            self.ticket_dao.tickets.remove(ticket)
          continue
        try: # link assignees
          assignee_id = ticket.get("assignee_id")
          if assignee_id == 'None':
            logging.debug(f"tck_id: {ticket['_id']} doesn't have an assignee")          
          else:
            assignee = SearchAPI.search_user_by_id(self.user_dao, assignee_id)
            logging.debug(f"linking assignee tck_id: {ticket['_id']} -> user_id {user['_id']}")
            assignee['tickets_assigned'].append(ticket)
        except Exception as e:
          logging.warning(f"{e}, can't link assignee to ticket!")
          logging.warning(f"assignee_id: {assignee_id} can't be found among registered users")
          if config.FULL_RELATIONAL:
            self.ticket_dao.tickets.remove(ticket)
          continue

# search logic
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

  def search_tickets(self, key_name, value):
    """Search users by all fields

    Keyword arguments:
    key_name -- name of field
    value -- value of field to search
    """

    logging.info(f"searching by: field='{key_name}',value='{value}'")
    Validator.validate_input(key_name, value)
    return SearchAPI.search_ticket_by_field(self.ticket_dao, key_name, value)

# exporter logic

  def export_org(self, results, export_format):
    """Exports Organization

    Keyword arguments:
    results -- resource to export
    export_format -- export type format
    """
    DataExporter.show_header('ORGANIZATION')
    if isinstance(results, ResultSet):
      org = results.item
      logging.debug(f"found: {org['name']}")
      if len(org['users']) > config.MAX_ITEMS_SCREEN | len(org['tickets']) > config.MAX_ITEMS_SCREEN:
        DataExporter.to_many_to_show()
        DataExporter.export_item(org, 'file')
      else:
        DataExporter.export_item(org, export_format)
    else:
      DataExporter.show_not_found(results)

  def export_user(self, results, export_format):
    """Exports User result

    Keyword arguments:
    user -- user to export
    export_format -- export type format
    """
    DataExporter.show_header('USER')
    if isinstance(results, ResultSet):
      user = results.item
      logging.debug(f"found: {user['name']}")
      DataExporter.export_item(user, export_format)
      org = SearchAPI.search_org_by_id(self.org_dao, user.get("organization_id"))
      DataExporter.show_org_relation(org, export_format)
    else:
      DataExporter.show_not_found(results)

  def export_ticket(self, results, export_format):
    """Exports Ticket object

    Keyword arguments:
    ticket -- ticket to export
    export_format -- export type format
    """
    DataExporter.show_header('TICKET')
    if isinstance(results, ResultSet):
      ticket = results.item
      logging.debug(f"found: {ticket['subject']}")
      DataExporter.export_item(ticket, export_format)
      submitter = SearchAPI.search_user_by_id(self.user_dao, ticket.get("submitter_id"))
      assignee = SearchAPI.search_user_by_id(self.user_dao, ticket.get("assignee_id"))
      DataExporter.show_user_relation(submitter, 'submitter', export_format)
      DataExporter.show_user_relation(assignee, 'assignee', export_format)
      org = SearchAPI.search_org_by_id(self.org_dao, ticket.get("organization_id"))
      DataExporter.show_org_relation(org, export_format)
    else:
      DataExporter.show_not_found(results)
