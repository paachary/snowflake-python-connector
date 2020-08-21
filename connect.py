import os
import snowflake.connector



# Before executing this python module, please ensure you execute 
# the following export / set commands in your OS command line.
# export SNOWFLAKE_PWD=<pwd>
# export SNOWFLAKE_USER=<user>
# export WAREHOUSE=<warehouse>
# export SNOWFLAKE_ACCOUNT=<account with cloud provider>

PASSWORD = os.getenv('SNOWFLAKE_PWD')
USERNAME = os.getenv('SNOWFLAKE_USER')
WAREHOUSE = os.getenv('WAREHOUSE')
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')

# Gets the version
ctx = snowflake.connector.connect(
    user = USERNAME,
    password = PASSWORD,
    account = ACCOUNT
    )
cs = ctx.cursor()
try:
    print("connected to account : {}, with user : {}".format(ACCOUNT,USERNAME))

    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print('Current version is {}'.format(one_row[0]))

    cs.execute(" USE ROLE sysadmin ")
    cs.execute(" USE DATABASE localdb ")
    cs.execute(" USE SCHEMA pipe_schema")


    cs.execute( " SHOW TABLES")
    print(" Printing the table :")
    for row in cs.fetchall():
        print("{}:{}:{}:{}".format(row[0],row[1],row[2],row[3]))

finally:
    cs.close()
ctx.close()
