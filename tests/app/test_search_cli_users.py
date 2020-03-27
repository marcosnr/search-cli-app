from click.testing import CliRunner
import pytest

from search_cli import search_cli, organisations, users, tickets

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

# users
def test_users_by_id(runner):
    result = runner.invoke(users, ["--field", "_id", "--value", "1"])
    assert result.exit_code == 0

def test_users_by_name(runner):
    result = runner.invoke(users, ["--field", "name", "--value", "Francisca Rasmussen"])
    assert result.exit_code == 0

def test_users_by_tags(runner):
    result = runner.invoke(users, ["--field", "tags", "--value", "Hartsville/Hartley"])
    assert result.exit_code == 0

def test_users_by_activity(runner):
    result = runner.invoke(users, ["--field", "active", "--value", "true"])
    assert result.exit_code == 0
