import os
import pytest
from data_loader import DataLoader

def test_load_org_file():
  current_dir = os.path.dirname(os.path.realpath(__file__))
  test_file = os.path.join(current_dir, 'resources', 'test_orgs.json')
  assert DataLoader._load_file(test_file)

def test_load_user_file():
  current_dir = os.path.dirname(os.path.realpath(__file__))
  test_file = os.path.join(current_dir, 'resources', 'test_users.json')
  assert DataLoader._load_file(test_file)

def test_load_ticket_file():
  current_dir = os.path.dirname(os.path.realpath(__file__))
  test_file = os.path.join(current_dir, 'resources', 'test_tickets.json')
  assert DataLoader._load_file(test_file)
