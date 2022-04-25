# Example Ingestion Pipeline

This is an example ingest meant to demonstrate how one might set up an ingestion
pipeline using this template repository. It should be deleted before this
repository or any of its ingests are used in a production environment.

## Getting started

1. Ensure that your development environment is set up according to
[the instructions](../../README.md#development-environment-setup).

2. Use the `TODO-Tree` VS Code extension or use the search tool to find occurances of
"`# DEVELOPER:`". Each instance of this requires your attention. Attend to all the
developer todos in this folder and remove the comment as you implement things. These
developer comments will need to be removed before the pipeline

3. As you are developing, try to follow best practices to save yourself (and others)
time in the future:
    - Commit your changes to git/github early and often to prevent accidental code loss.
    - Write tests as soon as possible and test often. When pushing changes to github
    all the tests in this repository will be run.
    - In general, try to write modular, resusable code to save your future self (and
    your teammates) some time. Comments are particularly useful when they explain
    **why** something was done, as opposed to *how* it was done.

4. You can run your code locally in VS Code by running the tests, or by running /
debugging the `runner.py` script at the top level of this repository.

5. When you have finished the ingest script your tests should pass, the code should be
formatted by `black`, there should be no `flake8` warnings (Use "`# noqa`" to disable
a specific line, if need be), and this `README.md` file should be updated to include a
description of your ingest pipeline for end-users, project maintainers, and curious
onlookers who may not be familiar with your work. Additionally, please remove this
section ("Getting Started") of the README.md file. If this has all been completed, then
commit and push your changes to your repository, sync it up with the upstream main
repository, and submit a pull request so that your changes can be reviewed and merged
into production.
