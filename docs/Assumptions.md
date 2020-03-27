# Assumptions and limitations

I asked by email for confirmation on the following, decided to go ahead assuming:

* Only first match will be returned (No mention that had to retrieve all existing hits in input data)

* Only full value match is accepted.

e.g.
- returning "mary" when searching only for "mary" 
will *NOT* return "mary", "Mary", "MarCos", "marc", "Amar" 

- searching for "Edgar Poe" will *NOT* return "Edgar A. Poe"

* Empty fields with are matched, but if the field being search is a list of items, like "tags" or "domain_names", if it's empty will *NOT* match
(Also ask for clarification so needed to assume the easier)

* Primary Keys "_id" must exist

* Regarding Foreing keys, I asked if it was a full relational data base or more towards a noSQL database. Didn't get confirmation, so tried to cater for both.By default item will load, but will not match for that field (e.g. orphan user not belonging to an organization). This can be enforced by modifiying `config.py` and setting `FULL_RELATIONAL = True`

* Assume I have access to the public Internet to download public libraries

* For big result queries export to json file is reccomended, but result will be split in 1 two 3 files, depending on relationships found (see Design for remediation)
