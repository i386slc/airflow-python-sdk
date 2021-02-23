"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

import logging

from test.integration.conftest import BCOLORS

from airflow_python_sdk.model.connection import Connection

conn_dict = {
    "connection_id": "test_connection",
    "conn_type": "FTP",
    "host": "host",
    "login": "login",
    "schema": "schema",
    "port": 10000,
    "password": "secret",
    "extra": "{'key': 'value'}",
}

INIT_CONN = Connection(**conn_dict)

conn_dict["conn_type"] = "SFTP"
conn_dict.pop("password")
UPDATED_CONN = Connection(**conn_dict)

def test_create_connections(connection_api_setup):
    """Test the post /connections API EP"""
    api_response = connection_api_setup.post_connection(INIT_CONN)
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

def test_update_connections(connection_api_setup):
    """Test the patch /connections/{connection_id} API EP"""
    api_response = connection_api_setup.patch_connection(
        "test_connection",
        UPDATED_CONN,
    )
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

def test_get_connection(connection_api_setup):
    """Test the get /connections/{connection_id} API EP"""
    api_response = connection_api_setup.get_connection("test_connection")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")
    assert api_response == UPDATED_CONN

def test_delete_connections(connection_api_setup):
    """Test the delete /connections/{connection_id} API EP"""
    api_response = connection_api_setup.delete_connection("test_connection")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")
