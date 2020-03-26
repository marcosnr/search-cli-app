# Global variables

# Logging
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
# Default log Level
# LOG_LEVEL = DEBUG
LOG_LEVEL = WARNING
LOG_FORMAT = '%(levelname)s:%(funcName)s:%(message)s'

# Default configuration
# DEFAULT_ORG_DATA = 'assets/test_orgs.json'
# DEFAULT_USER_DATA = 'assets/test_users.json'
# DEFAULT_TICKET_DATA = 'assets/test_tickets.json'
DEFAULT_ORG_DATA = 'assets/organizations.json'
DEFAULT_USER_DATA = 'assets/users.json'
DEFAULT_TICKET_DATA = 'assets/tickets.json'
DEFAULT_RESULT_URI = 'results'
DEFAULT_ORG_KEY_NAME = 'name'
DEFAULT_USER_KEY_NAME = 'name'
DEFAULT_TICKET_KEY_NAME = 'subject'
DEFAULT_OUT_FORMAT = 'yaml'
TS_SUFIX = "@%H_%M_%S_%f"
MAX_ITEMS_SCREEN = 9
# Whether to enforce FK need to exist, or are ignored.
# e.g. a user without an organization_id will not be loaded
FULL_RELATIONAL = False
