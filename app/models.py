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
    """simple customised string representation of this object"""
    return f"{len(self.organizations)}"


class UserDAO:
  """ Simple Data Access Object Pattern implementation
  to support Accessing User entities
  """

  def __init__(self):
    self.users = []

  def __str__(self):
    """simple customised string representation of this object"""
    return f"{len(self.users)}"


class TicketDAO:
  """ Simple Data Access Object Pattern implementation
  to support Accessing Ticket entities
  """

  def __init__(self):
    self.tickets = []

  def __str__(self):
    """simple customised string representation of this object"""
    return f"{len(self.tickets)}"
