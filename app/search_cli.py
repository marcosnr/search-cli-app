import click
import logging
import config

from search import SearchApp

logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


@click.group()
def search_app():
  pass

# search organizations --field '_id' --value 102
@click.command(help='search inside an organization ticketing system')
@click.option('--field', default='name', help='field name to search for')
@click.option('--value', required=True, help='value to search in the given field')
def organisations(field, value):

  logging.info(f"organisation by: field='{field}',value='{value}'")
  app = SearchApp()
  app.load_data()
  app.search_organisations(field, value)


if __name__ == '__main__':
  try:
    search_app.add_command(organisations)
    search_app()
  except Exception as e:
    logging.error("search error: {0}".format(e))
