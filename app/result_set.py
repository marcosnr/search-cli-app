import logging
import config

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class DefaultResultSet:
  """ Encapsulate data returned by a user search"""

  def __init__(self, field, value):
    """ If no results where found, sucess is False"""
    self.query_field = field
    self.query_value = value

  def __str__(self):
    """simple customised string representation of this object"""
    output = (f"Could not match: '{self.query_value}"
              f"with any field: '{self.query_field}'")
    return output


class ResultSet(DefaultResultSet):
  """ Item Result with search parameters and response"""

  def __init__(self, item, field, value):
    self.query_field = field
    self.query_value = value
    self.item = item

  def __str__(self):
    """simple customised string representation of this object"""
    output = (f"Requested field: {self.query_field}"
              f"| Requested value: {self.query_value}"
              f"| result(s): {len(self.item)}")
    return output
