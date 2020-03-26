from click.testing import CliRunner
import pytest

from search_cli import search_cli, organisations, users, tickets

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

# tickets
def test_tickets_by_id(runner):
    result = runner.invoke(tickets, ["--field", "_id", "--value", "436bf9b0-1147-4c0a-8439-6f79833bff5b"])
    assert result.exit_code == 0

def test_tickets_by_subject(runner):
    result = runner.invoke(tickets, ["--field", "subject", "--value", "A Catastrophe in Korea (North)"])
    assert result.exit_code == 0

def test_tickets_by_tags(runner):
    result = runner.invoke(tickets, ["--field", "tags", "--value", "Pennsylvania"])
    assert result.exit_code == 0
