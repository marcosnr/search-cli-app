# Zen CLI Search App

"Mies Van der Rohe's style" Search CLI App. 
Simple and modular text search match on relational json input data

```bash
./bin/search_cli --help
Usage: search_cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  organisations  search inside an organization ticketing system
  tickets        search for a ticket of an organization ticketing system
  users          search for a user of an organization ticketing system
```
## Setup

### Prerequisites

Python 3 installed on *Nix OS (Linux, Mac, WSL), and connection to the internet to download required libraries.
- Execute the following comand on a bash terminal

```bash
make
```
- more info on the automated build, run `make help`

## Usage

Begin a `pipenv shell` environment to ensure all runtime libraries are present (if you have already them in your system you may skip this):

```bash
[search-cli-app/]$ pipenv shell
```

Specify `--value` and (optional) `--field` arguments:

```bash
./bin/search_cli users --field role --value admin
```

Results will be shown in the console in human readable format (`yaml`)

* Alternatively you can specify to save them in a `.json` file, with `--export-format file`
(Recommended for big organizations and / or special character encoding)

```bash
./bin/search_cli organisations --value "Terrasys" --export-format file
```

### Notes

*  If `--field` is not provided, for organizations and users `name` will be assumed (`--field name`)

```bash
./bin/search_cli users --field '_id' --value 35
```

for tickets (`--field subject`) will be assumed. 

```bash
./bin/search_cli tickets --value "A Catastrophe in Micronesia"
```

* If your query has spaces or should match empty, surround it with quotes:
```bash
./bin/search_cli users --value "Woodard Burt"
```
or
```bash
./bin/search_cli tickets --field 'description' --value ''
```

* More info with `[subcommand] --help` 

```bash
./bin/search_cli organisations --help
```

* if you don't want to execute this `./bin/search_cli` or give `+x` permissions, all commands can be replaced with `python app/search_cli.py`, as in:

```bash
python app/search_cli.py organisations --help
```

## Input Data

The search app automatically loads provided data on:
- `assets/organizations.json`
- `assets/users.json`
- `assets/tickets.json`

If you want to provide other input, specify relative or full path in `config.py` file.

## Test Coverage

* Running the test suite

```bash
make test
```

* Linting is done with flake8

```bash
make test
```
* Security Scaning

```bash
make scan
```

## Asumptions

See: [/docs/Assumptions.md](/docs/Assumptions.md)

## Design principles and Roadmap

See: [/docs/Design.md](/docs/Design.md)