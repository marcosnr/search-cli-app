# High Level Design (HLD)

Explanation of design decisions and overall roadmap for this app

## Principles

* Extensibility - separation of concerns.
* Simplicity - aim for the simplest solution that gets the job done whilst remaining readable, extensible and testable.
* Test Coverage - breaking changes should break your tests.
* Performance - should gracefully handle a significant increase in amount of data provided (e.g 10000+ users).
* Robustness - should handle and report errors.
* *Security and automation* -In order to support all of the previous ones correctly

## MVC Architecture

View: CLI input console
Controller: Main class
Model: Data layer with DAO Pattern abstraction for extensibility of Datasources

### Extensibility Modules

By using the `Interface -> Implements` Pattern, Modules will be Implemented by the simplest possible representation, but later can be replaced by other implementation technologies without breaking the contract between modules. e.g.:
DAO Interface will be implemented by a simple data structure (collections). It can be backed by a more reliable DB Datasource in the future with minimum impact to the other modules.

### Sketch Diagram

In the Sketch below you can see the overall module architecture:

![Alt Module diagram](arch-sketch.png?raw=true "Module diagram")


## guidelines

* TDD Approach. First tests must fail, only then create back end that meets criteria
* Clear git commit history showing TDD 
* Early integration
* Early and clear documentation

## Road Map

1. Create Skeleton of Modules and check minimum search:
- Unit tests
- Simple CLI with test Stub data
- Main class to handle flow
- DAO class to handle queries
- Data stored in primitive variables
- Linting

2. Enhance with better I/O and validation
- Load Data from given json files
- basic Input / error validation

3. MVP of search capabilities
- Return full match on query of one simple item
- Association of list of items according to FKs 
- Return all related items for a hit

* Load testing 10k+ items

* Build Automation

* "Security job 0" principles as early as possible

* POC for Extensibility with in memory library:
  - [Marshmellow](https://marshmallow.readthedocs.io/en/stable/nesting.html)
  - JsonDB/MongoDB integration

