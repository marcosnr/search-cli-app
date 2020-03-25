import os
import sys
import pytest
import config

from data_exporter import DataExporter

@pytest.fixture
def search_results():
  test_results = {
      "_id": 101,
      "url": "http://initech.zendesk.com/api/v2/organizations/101.json",
      "external_id": "9270ed79-35eb-4a38-a46f-35725197ea8d",
      "name": "Enthaze",
      "domain_names": [
        "kage.com",
        "ecratic.com",
        "endipin.com",
        "zentix.com"
      ]
    }
  return search_results

def test_yaml_print(capsys,search_results):
    DataExporter.yaml_print(search_results)
    out, err = capsys.readouterr()
    assert  out !=''
    assert  err ==''
    
def test_yaml_print(capsys,search_results):
    DataExporter.yaml_print(search_results)
    out, err = capsys.readouterr()
    assert  "exporter" in out 
    assert  out !=''
    assert  err ==''

def test_exports_json_file(search_results):
  DataExporter.json_out(search_results)
  current_dir = os.path.dirname(os.path.realpath(__file__))
  assert os.path.isfile(config.DEFAULT_RESULT_URI)
