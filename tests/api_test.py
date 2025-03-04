import json

import pytest
import requests

from pansionat_site.Models.Liecensed_company import LicensedCompany
from utils.common_utilities import (
    compare_and_write_file,
    send_email_notification,
    send_windows_notification,
)

base_url = "https://license.gov.by/api/licenses/getAllPaged"


@pytest.mark.parametrize("activity", [78])
def test_new_company(activity, session):
    url = base_url
    params = {
        "number": "",
        "registerNumber": "",
        "unp": "",
        "activity": activity,
        "requests": "",
        "page": "1",
        "pageSize": "10",
    }
    try:
        response = session.get(url, params=params, timeout=(1, 5))
        assert response.status_code == 200
        json_data = json.loads(response.content)
        license_items = [
            LicensedCompany(
                id=item["id"],
                generated_number=item["generatedNumber"],
                activity_id=item["reActivityType"]["id"],
                activity_code=item["reActivityType"]["code"],
                activity_name=item["reActivityType"]["name"],
                unp=item["licenseHolder"]["unp"],
                holder_name=item["licenseHolder"]["name"],
            )
            for item in json_data["items"]
        ]
        company_names = [company.holder_name for company in license_items]
        is_updated = compare_and_write_file("List_api.txt", company_names)
        send_windows_notification(is_updated)
        send_email_notification(is_updated)
    except requests.exceptions.Timeout as e:
        print(f"Timed out: {e}")
