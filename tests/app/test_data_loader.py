import os
import pytest
from data_loader import DataLoader

def test_load_file():
  current_dir = os.path.dirname(os.path.realpath(__file__))
  test_file = os.path.join(current_dir, 'resources', 'orgs.json')
  assert DataLoader._load_file(test_file)

