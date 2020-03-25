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
      if value == 'None':
        org_dao.remove(org)
      logging.debug(f"'{org['name']}' ok, init users list...")
      org.update({'users': []})
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
      if value == 'None':
        user_dao.remove(user)
    # are there any remaining valid users?
    if int(f"{user_dao}") > 0:
      logging.info(f"loaded '{user_dao}' users correctly")
      return True
    else:
      raise Exception("users data wasn't loaded properly")

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
