# snowflake-python-connector

This repository provides a sample example of connecting to snowflake via snowflake connector for python

The script connects to snowflake account using the username and password specified by the user
via either the export or set commands on the command line of the appropriate OS.

The script then executes a use role, use database and use schema to navigate to a particular schema of a database.
It then lists all the tables available to the user via the role.
