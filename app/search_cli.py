import click
import logging
import config

from search import SearchApp

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


@click.group()
def search_app():
  pass


@click.command(help='search inside an organization ticketing system')
@click.option('--field', default='name', help='field name to search for')
@click.option('--value', required=True, help='value to search in the given field')
@click.option('--export_format', default='yaml', help='format to show results (json | yaml | file)')
def organisations(field, value, export_format):

  logging.debug(f"organisation by: field='{field}',value='{value}'")
  app = SearchApp()
  app.load_data()
  results = app.search_organisations(field, value)
  app.export(results, export_format)


if __name__ == '__main__':
  try:
    search_app.add_command(organisations)
    search_app()
  except Exception as e:
    logging.error("search error: {0}".format(e))
