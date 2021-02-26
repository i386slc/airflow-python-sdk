"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

import logging

from test.integration.conftest import BCOLORS


def test_get_pools(pool_api_setup):
    """Test the /pools API EP"""
    api_response = pool_api_setup.get_pools(
        limit=100,
        offset=0,
    )
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")
