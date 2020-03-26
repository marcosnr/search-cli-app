import json
import copy
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

  @staticmethod
  def export_item(item, export_format):
    """Exports Model Item

    Keyword arguments:
    item -- resource to export
    export_format -- export type format
    """
    logging.debug(f"format: '{export_format}' ")
    if export_format == 'json':
      DataExporter.pretty_print(item)
    elif export_format == 'yaml':
      DataExporter.yaml_print(item)
    elif export_format == 'file':
      DataExporter.json_out(item)
    else:
      raise Exception("Export format not supported")

  @staticmethod
  def show_org_relation(org, export_format):
      print(f"-------> Ticket belongs to ORG: [{org['name']}]::")
      copy_org = copy.deepcopy(org)
      del copy_org['users']
      del copy_org['tickets']
      DataExporter.export_item(copy_org, export_format)

  @staticmethod
  def show_not_found(results):
    print(f"Oops! 'quote the Raven...'404'...")
    print(f"{results} found, do you want to try again?")
