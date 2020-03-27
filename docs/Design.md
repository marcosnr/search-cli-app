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

## Future backlog (e.g. known issues in the present)

* friendly yaml  encode well in urf8 needs some love for special characters
* Export json files for big queries as only one result
* Use mocks to increase test performance and proper encapsulation
* Refactor code to comply with DRY guidelines
* Controller class big, should be refactored in smaller modules
* Command to load other input from the given one
* Custom  exceptions for not found and type of queries
* Input validation (proper email, url, timestamp, etc)
* Search returns all relevant hits
* Search for a user field inside an org (recursive search)
* Search by time range
* Makefile validate prerequisites and fail gracefully
* CLI Integration tests capturing ouptut print with utf8 encoding proper



* POC for Extensibility with in memory library:
  - [Marshmellow](https://marshmallow.readthedocs.io/en/stable/nesting.html)
  - JsonDB/MongoDB integration

