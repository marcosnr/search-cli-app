import logging
import config

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class Validator:
  """ Simple Input Validation logic"""

  @staticmethod
  def validate_org_data(org_dao):
    """Organisation model validation"""
    logging.info(f"loaded '{org_dao}' organisations correctly")
    if int(f"{org_dao}") > 0:
      return True
    else:
      raise Exception("organisation data wasn't loaded properly")

  @staticmethod
  def validate_user_data(user_dao):
    """User Model validation"""
    logging.info(f"loaded '{user_dao}' users correctly")
    if int(f"{user_dao}") > 0:
      return True
    else:
      raise Exception("user data wasn't loaded properly")

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
