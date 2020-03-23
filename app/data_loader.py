import json
import logging
import config

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)

class DataLoader:
  """Loads Input files to search environment"""

  @staticmethod
  def _load_file (uri):
    """Loads dictionary from a local json file.

    Keyword arguments:
    uri -- full or relative resource path and json file name
    """
    with open(uri, 'r') as f:
      json_dict = json.load(f)
    return json_dict