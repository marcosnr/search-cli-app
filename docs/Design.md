# High level Design

## MVC Architecture

View: CLI input console
Controller: Main class
Model: Data layer with DAO Pattern abstraction for extensibility of Datasources

### Extensibility Modules

By using the Interface -> Implements Pattern, Modules will be Implemented by the simplest possible representation, but later can be replaced by other implementation technologies without breaking the contract between modules. e.g.:
DAO Interface will be implemented by a simple Data structure, can be backed by a more reliable DB Datasource in the future.

### Sketch Diagram

In the Sketch below you can see the overall Module roadmap:

![Alt Module diagram](arch-sketch.png?raw=true "Module diagram")

## Road Map

1. Create Skeleton of Modules and check minimum search:
- Unit tests
- Simple CLI with test Stug data
- Main class to handle flow
- DAO class to handle queries
- Data stored in primitive variables 

2. Enhance with better I/O and validation
- Load Data from given json files
- basic Input / error validation

(Nice to have if times allows)

3. Build automation

4. Load testing 10k+ items

5. POC for Extensibility with in memory JsonDB/MongoDB interaction

6. Show security awareness as early as possible


## Architecture principles

1. Extensibility - separation of concerns.
2. Simplicity - aim for the simplest solution that gets the job done whilst remaining readable, extensible and testable.
3. Test Coverage - breaking changes should break your tests.
4. Performance - should gracefully handle a significant increase in amount of data provided (e.g 10000+ users).
5. Robustness - should handle and report errors.

## Extra guidelines

* TDD Approach. First tests must fail, only then create back end that meets criteria
* Clear git commit history showing TDD 
* Early integration
* Early and clear documentation

## Assumptions

I asked for confirmation on the following, while I get feedback assuming:

1. "full value matching is fine" assertion =  only full value match is accepted.

e.g. returning "mary" when searching only for "mary" 
will *NOT* return "mary", "Mary", "MarCos", "marc", "Amar" 

2. Non Id Fields must exist
e.g. App will check for:
"description" : ""
"description" : null
But will not check if "description" exist at all in a given input

3. assume I have access to the public Internet to download public libraries

4. Overall, focusing on  the "Dev side of things". 
Nonetheless, DevOps = Infrastructure-as-Code, and everything on the "Ops side of things"
like pipelines, stages, connectivity, build, Security Scanning etc. can and should be coded / tested as well... just like a "functional code", and from day 0!