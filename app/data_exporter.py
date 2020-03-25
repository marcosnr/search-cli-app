import json
import logging
import config
import yaml

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


class DataExporter:
  """Export search results in human readable format"""

  @staticmethod
  def yaml_print(search_result):
    """prints in a human friendly manner (YAML) a search result object

    Keyword arguments:
    search_result -- result (Dictionary)
    """

    logging.debug(f"items: {type(search_result)}")
    print(yaml.dump(search_result))

  @staticmethod
  def pretty_print(search_result):
    """prints in a human friendly manner (JSON) a search result object

    Keyword arguments:
    search_result -- result (Dictionary)
    """

    logging.debug(f"items: {len(search_result)}")
    print(json.dumps(search_result, indent=2, default=str))

  @staticmethod
  def json_out(search_result):
    """exports a human friendly manner (JSON) a search result object
    Important when results are are to big to be displayed in the console

    Keyword arguments:
    search_result -- result (Dictionary)
    """

    logging.debug(f"items: {type(search_result)}")
    jsonpretty = json.dumps(search_result, indent=2, default=str)
    with open(config.DEFAULT_RESULT_URI, 'w') as outfile:
      json.dump(jsonpretty, outfile)
