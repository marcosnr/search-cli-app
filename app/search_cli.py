import click
import logging
import config

from search_ctl import SearchApp

logger = logging.getLogger()
# file
fh = logging.FileHandler(config.LOG_FILE)
fh.setLevel(config.FILE_LOG_LEVEL)
# console
ch = logging.StreamHandler()
ch.setLevel(config.LOG_LEVEL)
# create formatter and add it to the handlers
formatter = logging.Formatter(config.LOG_FORMAT)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


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
@click.option('--export-format',
              default=config.DEFAULT_OUT_FORMAT,
              help='format to show results (yaml | json | file) [default:' + config.DEFAULT_OUT_FORMAT + ']')
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
@click.option('--export-format',
              default=config.DEFAULT_OUT_FORMAT,
              help='format to show results (yaml | json | file) [default:' + config.DEFAULT_OUT_FORMAT + ']')
def users(field, value, export_format):

  logging.debug(f"users by: field='{field}', value='{value}'")
  app = SearchApp()
  app.load_data()
  results = app.search_users(field, value)
  logging.debug(f"results={results}")
  app.export_user(results, export_format)


@click.command(help='search for a ticket of an organization ticketing system')
@click.option('--field',
              default=config.DEFAULT_TICKET_KEY_NAME,
              help='field name to search for [default:' + config.DEFAULT_TICKET_KEY_NAME + ']')
@click.option('--value',
              required=True,
              help='value to search in the given field')
@click.option('--export-format',
              default=config.DEFAULT_OUT_FORMAT,
              help='format to show results (yaml | json | file) [default:' + config.DEFAULT_OUT_FORMAT + ']')
def tickets(field, value, export_format):

  logging.debug(f"tickets by: field='{field}', value='{value}'")
  app = SearchApp()
  app.load_data()
  results = app.search_tickets(field, value)
  logging.debug(f"results={results}")
  app.export_ticket(results, export_format)


if __name__ == '__main__':
  try:
    search_cli.add_command(organisations)
    search_cli.add_command(users)
    search_cli.add_command(tickets)
    search_cli()
  except Exception as e:
    logging.error("command error: {0}".format(e))
