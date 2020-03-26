import logging
import config

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class Validator:
  """ Simple Input Validation logic"""

  @staticmethod
  def validate_org_data(org_dao):
    """Organisation model validation"""
    logging.debug(f"validating '{org_dao}' organisations...")
    for org in org_dao.organizations:
      value = org.get('_id')
      if value is None:
        logging.warning(f"'{org.get('name')}' doesn't have '_id' NOT loading!")
        org_dao.remove(org)
        continue
      logging.debug(f"'{org.get('name')}' ok, init users list...")
      # creating future relationship holders
      org.update({'users': []})
      org.update({'tickets': []})
    # are there any remaining valid orgs?
    if int(f"{org_dao}") > 0:
      logging.info(f"loaded '{org_dao}' organisations correctly")
      return True
    else:
      raise Exception("organisation data wasn't loaded properly")

  @staticmethod
  def validate_user_data(user_dao):
    """User Model validation"""
    logging.debug(f"validating '{user_dao}' users")
    for user in user_dao.users:
      value = user.get('_id')
      if value is None:
        logging.warning(f"'{user.get('name')}' doesn't have '_id' NOT loading!")
        user_dao.remove(user)
        continue
      # creating future relationship holders
      user.update({'tickets_assigned': []})
      user.update({'tickets_submitted': []})
    # are there any remaining valid users?
    if int(f"{user_dao}") > 0:
      logging.info(f"loaded '{user_dao}' users correctly")
      return True
    else:
      raise Exception("users data wasn't loaded properly")

  @staticmethod
  def validate_ticket_data(ticket_dao):
    """Ticket Model validation"""
    logging.debug(f"validating '{ticket_dao}' tickets")
    for ticket in ticket_dao.tickets:
      value = ticket.get('_id')
      if value is None:
        logging.warning(f"'{ticket.get('subject')}' doesn't have '_id' NOT loading!")
        ticket_dao.remove(ticket)
        continue
    # are there any remaining valid tickets?
    if int(f"{ticket_dao}") > 0:
      logging.info(f"loaded '{ticket_dao}' tickets correctly")
      return True
    else:
      raise Exception("tickets data wasn't loaded properly")

  @staticmethod
  def validate_input(key_name, value):
    if key_name == '':
      logging.info(f"using '{config.DEFAULT_ORG_KEY_NAME}' as default field")
      key_name = config.DEFAULT_ORG_KEY_NAME
    if isinstance(value, str):
      if value.lower() == 'true':
        logging.info(f"transforming 'true' text boolean input")
        value = True
      elif value.lower() == 'false':
        logging.info(f"transforming 'false' text boolean input")
        value = False
    if value is None:
      raise Exception("search value is invalid / null")
