from click.testing import CliRunner
import pytest

from search_cli import search_cli, organisations, users

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

#organisations
def test_organisations_by_id(runner):
    result = runner.invoke(organisations, ["--field", "_id", "--value", "102"])
    assert result.exit_code == 0

def test_organisations_by_name(runner):
    result = runner.invoke(organisations, ["--field", "name", "--value", "Enthaze"])
    assert result.exit_code == 0

def test_organisations_by_details(runner):
    result = runner.invoke(organisations, ["--field", "details", "--value", "Non profit"])
    assert result.exit_code == 0

def test_organisations_no_field(runner):
    result = runner.invoke(organisations, ["--field", "noop", "--value", "Enthaze"])
    assert result.exit_code == 0

def test_organisations_no_value(runner):
    result = runner.invoke(organisations, ["--field", "name", "--value", "noop"])
    assert result.exit_code == 0

def test_organisations_by_missing_optional(runner):
    result = runner.invoke(organisations, ["--value", "102"])
    assert result.exit_code == 0

def test_organisations_by_missing_required_argument(runner):
    result = runner.invoke(organisations, ["--field", "name"])
    assert result.exit_code == 2

def test_organisations_by_empty_details(runner):
    result = runner.invoke(organisations, ["--field", "details", "--value", ""])
    assert result.exit_code == 0

def test_organisations_by_tags(runner):
    result = runner.invoke(organisations, ["--field", "tags", "--value", "Fulton"])
    assert result.exit_code == 0

#users
def test_users_by_id(runner):
    result = runner.invoke(users, ["--field", "_id", "--value", "75"])
    assert result.exit_code == 0

def test_users_by_name(runner):
    result = runner.invoke(users, ["--field", "name", "--value", "Francisca Rasmussen"])
    assert result.exit_code == 0

def test_users_by_tags(runner):
    result = runner.invoke(users, ["--field", "tags", "--value", "Hartsville/Hartley"])
    assert result.exit_code == 0

def test_users_by_activity(runner):
    result = runner.invoke(users, ["--field", "active", "--value", "false"])
    assert result.exit_code == 0
