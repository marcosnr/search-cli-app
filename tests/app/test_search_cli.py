from click.testing import CliRunner
import pytest

from search_cli import search_cli, organisations

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_run(runner):
    result = runner.invoke(organisations,["--field", "_id", "--value", "102"])
    assert result.exit_code == 0
