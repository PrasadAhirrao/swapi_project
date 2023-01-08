import pymysql
import yaml
import toml
from pymysql import Connection


def get_db_conn() -> Connection:
    """
    Returns connection object of database "starwarsDB", for user "root", host "localhost".
    :return: connection object of pymysql
    """
    # connection to database
    with open("settings/secrets.yaml") as creds:
        doc = yaml.load(creds, Loader=yaml.FullLoader)

    connection = pymysql.connect(**doc)
    # breakpoint()
    print(f"Connected to MySQL database - '{connection.db.decode()}'")  # prints database name

    return connection


def get_db_conn_toml() -> Connection:
    with open("settings/secrets.toml") as creds:
        doc = toml.load(creds)
        config = doc.get("mysqldb")
        connection = pymysql.connect(**config)

    print(f"Connected to MySQL database - '{connection.db.decode()}'")  # prints database name
    return connection


# filename = "settings\secrets.yaml"
# c_file = __file__  # current file path
# c_dir = os.path.dirname(c_file)  # current directory
# abs_path = os.path.join(c_dir, filename)  # creates absolute path out of
# current directory and given file name
# print(f"current file - {c_file}")
# print(f"current directory - {c_dir}")
# print(f"absolute file path - {abs_path}")
# print(os.path.exists(abs_path))  # checks if given file path exists or not

if __name__ == "__main__":
    get_db_conn_toml()