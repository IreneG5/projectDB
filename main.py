import random
from database.mysql import MySQLDatabase
from settings import db_config

"""
Retrieve the settings from the
`db_config` dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""
if __name__ == "__main__":
    db = MySQLDatabase(db_config.get('db_name'),
                       db_config.get('user'),
                       db_config.get('pass'),
                       db_config.get('host'))

    """
    # Get all the records from
    # the people table
    results = db.select('people')
    print "Selecting Rows"
    for row in results:
        print row

    # Selecting columns with named tuples
    results = db.select('people',
                        columns=['id', 'first_name'], named_tuples=True)
    print "Selecting Columns"
    for row in results:
        print row.id, row.first_name

    # We can also do more complex queries using `CONCAT`
    # and `SUM`
    people = db.select('people', columns=["CONCAT(first_name, ' ', second_name) "
                        " AS full_name", "SUM(amount)AS total_spend"],
                        named_tuples=True, where="people.id=1",
                        join="orders ON people.id=orders.person_id")
    print ("CONCAT & SUM")
    for person in people:
        print person.full_name, "spent ", person.total_spend

    # Inserting an order
    # db.insert('orders', person_id="2", amount="120.00")

    # Updating a person
    # person = db.select('people', named_tuples=True)[0]
    # db.update('profiles', where="person_id=%s" % person.id,
    #      address="1a another street")

    # Deleting a record
    # person = db.select('people', named_tuples=True)[0]
    # db.delete('orders', person_id="=%s" % person.id, id="=1")


    # Get all the available tables for
    # our database and print them out.
    tables = db.get_available_tables()
    print tables

    # Get all the available columns for our
    # articles table and print them out
    columns = db.get_columns_for_table('profiles')
    print columns

    columns = db.get_columns_for_table('orders')
    print columns


    # Get all the records from
    # the people table
    all_records = db.select('people')
    print "All records: %s" % str(all_records)

    # Get all of the records from
    # the people table but only the
    # `id` and `first_name` columns
    column_specific_records = db.select('people', ['id', 'first_name'])
    print "Column specific records: %s" % str(column_specific_records)

    # Select data using the WHERE clause
    where_expression_records = db.select('people', ['first_name'],
                                         where="first_name='John'")
    print "Where Records: %s" % str(where_expression_records)

    # Select data using the WHERE clause and
    # the JOIN clause
    joined_records = db.select('people', ['first_name'],
                               where="people.id=3",
                               join="orders ON people.id=orders.person_id")
    print "Joined records: %s" % str(joined_records)

    # Delete a record from the database
    db.delete('orders', id="=3")

    # We can also use multiple WHERE clauses!
    db.delete('orders', id=">4", amount=">1")
    """

    """Challenge A
    Using the AVG(), select a person from your people table and get
     the average amount they spend and, at the same time, create a column
      that reads, [first_name] spends . Then print out the columns
      to provide the answers in the terminal."""

    people = db.select('people', columns=['first_name', "AVG(amount) AS avg_spend"],
                       named_tuples=True,
                       where="people.id=1",
                       join="orders ON people.id=orders.person_id")
    print "CHALLENGE A"
    for person in people:
        print person.first_name, "spends", person.avg_spend

    """ Challenge B:
    Create a new person in the people table and add in a
    profile row and two orders of random value."""


    #db.insert('people', first_name="Bruce", second_name="Wayne", DOB='STR_TO_DATE("20/09/1983", "%d/%m/%Y")')
    results = db.select('people')
    print "Selecting Rows"
    for row in results:
        print row

    new_person=db.select('people', ['id', 'first_name'], where="people.first_name='Peter'", named_tuples=True)
    new_person=new_person[0]
    print "new person"
    print new_person

    #db.insert('profiles',  person_id="%s" % new_person.id, address="Peter Address", )

    #db.insert('orders', person_id="%s" % new_person.id, amount="%s" % random.randint(2, 18))
    #db.insert('orders', person_id="%s" % new_person.id, amount="%s" % random.randint(2, 18))

    orders = db.select('orders', where='person_id=%s' % new_person.id)
    for order in orders:
            print order

    """Challenge C:
    Once you have added them in use select to get their full name and the minimum
    amount they have spent."""

    person = db.select('people', columns=["CONCAT(first_name, ' ', second_name)" "AS full_name",
                                          "MIN(amount)" "AS min_spend"],
                                            named_tuples=True, where="people.id=%s" %new_person.id,
                                            join="orders ON people.id=orders.person_id")

    print person

    """Challenge D:
    Choose a person and update ALL of his orders to have the amount 20.02."""

    person = db.select('people', where='first_name="Peter"', named_tuples=True)[0]
    print person

    orders = db.select('orders', named_tuples=True, where="person_id=%s" % person.id)
    for order in orders:
        db.update('orders', where="id=%s" % order.id, amount="20.02")
        print order










