import argparse
import mysql.connector

MYSQL_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'dataset'
}


def get_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)


def insert_record(values):
    cnx = get_connection()
    cursor = cnx.cursor()

    add_dataset = ("INSERT INTO dataset_record "
                   "(dataset_name, dataset_description, dataset_owner, dataset_tags) "
                   "VALUES (%s, %s, %s, %s)")

    data_dataset = tuple(values)

    cursor.execute(add_dataset, data_dataset)

    cnx.commit()

    cursor.close()
    cnx.close()


def query_table():
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "SELECT dataset_name, dataset_description, dataset_owner, dataset_tags FROM dataset_record"

    cursor.execute(query)

    for row in cursor.fetchall():
        print("dataset_name={}, dataset_description={}, dataset_owner={}, dataset_tags={}".format(
                    row[0], row[1], row[2], row[3]))

    cnx.close()


def main():
    parser = argparse.ArgumentParser(description='MySQL query interface for dataset_record table')
    parser.add_argument('-i', '--insert', nargs=4, help='insert the record in the dataset_record table')
    parser.add_argument('-s', '--select', action='store_true', help='query the dataset_record table')
    args = parser.parse_args()

    if args.insert and args.select:
        print("Please choose one operation")

    if args.insert:
        insert_record(args.insert)
        print("Record inserted!")

    if args.select:
        query_table()


if __name__ == "__main__":
    main()
