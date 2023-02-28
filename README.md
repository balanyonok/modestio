# modestio
A family project for a cat shelter.

Written in Python with Django.
Potentially convertible into a single-page app in React with RESTful API.

## Stakeholders & Goals

* Business owner

  * get a shelter cat adopted by a family
  * collect donations
  * current expenses
  * specific shelter-wide projects
  * specific animals

* Customer

  * choose and adopt a cat
  * put a stray cat to a shelter
  * donate money or stuff

## Development Policies

* testing: maybe only for selected stories, explicitly planned
* merging: only via code reviews (doesn’t matter who merges)
* language: English

## Development: How To

Install [pre-commit](https://pre-commit.com) and its hooks:
```
$ pip install pre-commit
$ pre-commit install
```
Install `tox` and run it:

```
$ tox
```
