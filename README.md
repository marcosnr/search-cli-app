# search-cli-app

Mies Van der Rohe's style Search CLI App. 
Simple and modular full text search match on relational json input data

## Setup

### Prerequisites

Python 3 installed on *Nix machine (Linux, Mac)

```bash
make install 
```

## Test Coverage

```bash
pipenv shell
PYTHONPATH=app:$PYTHONPATH pytest
```

## Design principles and Roadmap

See: [/docs/Design.md](/docs/Design.md)