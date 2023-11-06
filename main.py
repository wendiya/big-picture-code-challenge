"""Runs the webserver and creates database"""

from argparse import ArgumentParser
import os

from application.configuration import Configuration
from application.server.server import Server
from application.database.database import create_database

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def main(config_path):
    configuration = Configuration(config_path) # instance of configuration class

    create_database(path_to_database=os.path.join(ROOT, configuration.path_to_database),
                    table_name=configuration.table_name)

    server = Server(table_name=configuration.table_name,
                    path_to_database=os.path.join(ROOT, configuration.path_to_database))
    server.define_database_configurations()
    server.connect_to_database()
    server.define_server_routers() # define routers that process requests to website
    server.app.run()


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        '-c',
        '--config_path',
        metavar='path/to/file',
        type=str,
        help='A path to the configuration.json file. Default is \'./configuration.json\'.',
        default='configuration.json'
    )
    args = parser.parse_args()
    main(args.config_path)
