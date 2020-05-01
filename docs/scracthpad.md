python app/search_cli.py
python app/search_cli.py organisations --help
python app/search_cli.py organisations --help
python app/search_cli.py organisations --field '_id' --value 102
python app/search_cli.py organisations --field '_id' --value 102
# INFO:root:Search Organizations APP MVP
python app/search_cli.py organisations --field '_id' --value 102 --export_format json
# INFO:root:initialising app...

# INFO:root:loading data...
python app/search_cli.py organisations --field 'name' --value 'Enthaze'
# INFO:root:loaded '25' organizations
python app/search_cli.py organisations --field 'details' --value ''
# INFO:root:searching by: attribute_name='_id',value='102'
python app/search_cli.py organisations --field 'noop' --value 'bad'
# INFO:root:search_org_by_id: 102
python app/search_cli.py organisations --field 'tags' --value 'Fulton'
# INFO:root:found: Nutralab
python app/search_cli.py organisations --field 'domain_names' --value 'dadabase.com'
TEST_NAME='test_search_cli.py'
TEST_NAME='test_search_api.py'
TEST_NAME='test_search_ctl.py'
TEST_NAME='test_validator.py'
py.test tests/app/${TEST_NAME}