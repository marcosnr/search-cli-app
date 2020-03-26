import os
import json
import copy
import logging
import config
import yaml
from datetime import datetime

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
    current_dir = os.path.dirname(os.path.realpath(__file__))
    curr_path = os.path.join(current_dir, config.DEFAULT_RESULT_URI)
    full_path = curr_path + datetime.strftime(datetime.now(), config.TS_SUFIX) + '.json'
    print(f"...Exporting search results to-> {full_path}")
    try:
      with open(full_path, 'w+', encoding='utf-8') as outfile:
        json.dump(search_result, outfile)
    except Exception:
      raise Exception(f"'{full_path}' could not be written")

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
      print(f"******* Ticket belongs to ORG: [{org['name']}]::")
      copy_org = copy.deepcopy(org)
      del copy_org['users']
      del copy_org['tickets']
      DataExporter.export_item(copy_org, export_format)

  @staticmethod
  def show_user_relation(user, type, export_format):
    if type == 'submitter':
        print(f"<<<<< Ticket was submitted by: [{user['name']}]::")
    else:
        print(f">>>>> Ticket is assigned to: [{user['name']}]::")
    copy_user = copy.deepcopy(user)
    del copy_user['tickets_assigned']
    del copy_user['tickets_submitted']
    DataExporter.export_item(copy_user, export_format)

  @staticmethod
  def show_not_found(results):
    print(f"Oops! 'quote the Raven...'404'...")
    print(f"{results} found, do you want to try again?")

  @staticmethod
  def show_header(type):
    print(f"\n\n________SEARCH {type} RESULTS__________")

  @staticmethod
  def to_many_to_show():
    print(f"\n\n !!RSI warning!!"
          f"Search results are too big to show on the screen"
          f"defaults to save results in a file")
