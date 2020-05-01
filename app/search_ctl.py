import logging
import config
import copy
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
    logging.debug(">>> linking users with organizations...")
    for user in self.user_dao.users:
      for org in self.org_dao.organizations:
        try:
          organization_id = user.get("organization_id")
          if organization_id is None:
            logging.warning(f"user {user.get('_id')} doesn't have an organization_id")
            if config.FULL_RELATIONAL:
              self.user_dao.users.remove(user)
            break
          else:
            org = SearchAPI.search_org_by_id(self.org_dao, organization_id)
            self.add_user_to_org(user, org)
        except Exception as e:
          logging.warning(f"{e}, can't link user id {user.get('_id')}")
          if config.FULL_RELATIONAL:
            self.user_dao.users.remove(user)
          continue

  def add_user_to_org(self, user, org):
    # Check user has not been added already...
    logging.debug(f"adding {user.get('name')} to {org.get('name')}")
    existing_users = org.get('users')
    # base case
    if existing_users is None:
      org['users'].append(user)
    else:
      for existing_user in existing_users:
        if str(existing_user.get("_id")) == str(user.get("_id")):
          logging.debug(f"{user.get('_id')} exists")
          return True
      org['users'].append(user)
      logging.debug(f"ok: {user.get('name')} -> {org.get('name')}")
    # a new one, let's add it

  def link_tickets(self):
    """Link tickets to their respective organizations and users"""
    logging.debug("+++ linking tickets with organizations...")
    for ticket in self.ticket_dao.tickets:
      tck_id = ticket.get('_id')
    # 1. link tickets to orgs
      try:
        organization_id = ticket.get("organization_id")
        if organization_id is None:
          logging.debug(f"tck = {tck_id} doesn't have an organization_id")
        else:
          logging.debug(f"1.t->o {tck_id} -> {organization_id}")
          org = SearchAPI.search_org_by_id(self.org_dao, organization_id)
          org['tickets'].append(ticket)
      except Exception as e:
        logging.warning(f"{e}, can't link tck {tck_id}")
        if config.FULL_RELATIONAL:
          self.ticket_dao.tickets.remove(ticket)
          continue
      # 2. link tickets to submitters
      try:
        submitter_id = ticket.get("submitter_id")
        if submitter_id is None:
          logging.debug(f"tck = {tck_id} doesn't have a submitter")
        else:
          submitter = SearchAPI.search_user_by_id(self.user_dao, submitter_id)
          logging.debug(f"2.t->s | tck = {tck_id} -> submitter_id {submitter_id}")
          submitter['tickets_submitted'].append(ticket)
      except Exception as e:
        logging.warning(f"submitter {e} , can't link tck {tck_id}")
        if config.FULL_RELATIONAL:
          self.ticket_dao.tickets.remove(ticket)
          continue
      # 3. link tickets to assignees
      try:
        assignee_id = ticket.get("assignee_id")
        if assignee_id is None:
          logging.debug(f"tck = {tck_id} doesn't have an assignee")
        else:
          assignee = SearchAPI.search_user_by_id(self.user_dao, assignee_id)
          logging.debug(f"+3.t->a | tck = {tck_id} -> assignee_id {assignee_id}")
          assignee['tickets_assigned'].append(ticket)
      except Exception as e:
        logging.warning(f"assignee {e} , can't link tck {tck_id}")
        if config.FULL_RELATIONAL:
          self.ticket_dao.tickets.remove(ticket)

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
      logging.debug(f"printing org: {org.get('name')}")
      # avoiding printing tickets twice, sinced linked to orgs and to users
      copy_org = copy.deepcopy(org)
      copy_users = copy_org.get('users')
      for copy_user in copy_users:
        tickets_assigned = copy_user.get("tickets_assigned")
        if tickets_assigned is not None:
          del copy_user['tickets_assigned']
        tickets_submitted = copy_user.get("tickets_submitted")
        if tickets_submitted is not None:
          del copy_user['tickets_submitted']
      DataExporter.export_item(copy_org, export_format)
    else:
      DataExporter.show_not_found(results)

  def export_user(self, results, export_format):
    """Exports User result

    Keyword arguments:
    user -- user to export
    export_format -- export type format
    """
    logging.info(f"show_header")
    DataExporter.show_header('USER')
    if isinstance(results, ResultSet):
      user = results.item
      logging.debug(f"found: {user.get('name')}")
      DataExporter.export_item(user, export_format)
      organization_id = user.get("organization_id")
      if organization_id is None:
        logging.warning(f"{user.get('_id')} doesn't have an organization_id")
      else:
        org = SearchAPI.search_org_by_id(self.org_dao, user.get("organization_id"))
        # DataExporter.show_org_relation(org, export_format)
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
      logging.debug(f"printing ticket: {ticket.get('_id')}")
      DataExporter.export_item(ticket, export_format)
      logging.debug(f"printing submitter..")
      submitter_id = ticket.get("submitter_id")
      if submitter_id is None:
        logging.info(f"tck = {ticket.get('_id')} doesn't have a submitter")
      else:
        submitter = SearchAPI.search_user_by_id(self.user_dao, submitter_id)
        DataExporter.show_user_relation(submitter, 'submitter', export_format)
      logging.debug(f"printing assignee...")
      assignee_id = ticket.get("assignee_id")
      logging.debug(f"assignee_id {assignee_id}..")
      if assignee_id is None:
        logging.debug(f"tck = {ticket.get('_id')} doesn't have an assignee")
      else:
        assignee = SearchAPI.search_user_by_id(self.user_dao, assignee_id)
        DataExporter.show_user_relation(assignee, 'assignee', export_format)
      # print org
      organization_id = ticket.get("organization_id")
      if organization_id is None:
        logging.warning(f"{ticket.get('_id')} doesn't have an organization_id")
      else:
        org = SearchAPI.search_org_by_id(self.org_dao, organization_id)
        DataExporter.show_org_relation(org, export_format)
    else:
      DataExporter.show_not_found(results)
