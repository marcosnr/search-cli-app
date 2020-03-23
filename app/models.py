import logging
import config

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class OrganizationDAO:
  """ Simple Data Access Object Pattern implementation
  to support Accessing Organization type entities
  """

  def __init__(self):
    self.organizations = []

  def __str__(self):
    return f"{len(self.organizations)}"
