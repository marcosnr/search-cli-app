import click
import logging
import config

from search_ctl import SearchApp

logging.basicConfig(format=config.LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL)


@click.group()
def search_cli():
  pass


@click.command(help='search inside an organization ticketing system')
@click.option('--field',
              default=config.DEFAULT_ORG_KEY_NAME,
              help='field name to search for [default:' + config.DEFAULT_ORG_KEY_NAME + ']')
@click.option('--value',
              required=True,
              help='value to search in the given field')
@click.option('--export_format',
              default=config.DEFAULT_OUT_FORMAT,
              help='format to show results (yaml |json | file) [default:' + config.DEFAULT_OUT_FORMAT + ']')
def organisations(field, value, export_format):

  logging.debug(f"organisation by: field='{field}', value='{value}'")
  app = SearchApp()
  app.load_data()
  results = app.search_organisations(field, value)
  logging.debug(f"results={results}")
  app.export_org(results, export_format)


@click.command(help='search for a user of an organization ticketing system')
@click.option('--field',
              default=config.DEFAULT_USER_KEY_NAME,
              help='field name to search for [default:' + config.DEFAULT_USER_KEY_NAME + ']')
@click.option('--value',
              required=True,
              help='value to search in the given field')
@click.option('--export_format',
              default=config.DEFAULT_OUT_FORMAT,
              help='format to show results (yaml |json | file) [default:' + config.DEFAULT_OUT_FORMAT + ']')
def users(field, value, export_format):

  logging.debug(f"users by: field='{field}', value='{value}'")
  app = SearchApp()
  app.load_data()
  results = app.search_users(field, value)
  logging.debug(f"results={results}")
  app.export_user(results, export_format)


if __name__ == '__main__':
  try:
    search_cli.add_command(organisations)
    search_cli.add_command(users)
    search_cli()
  except Exception as e:
    logging.error("command error: {0}".format(e))
