import pytest
import requests

TEST_HOST = "http://127.0.0.1:8000"


@pytest.mark.parametrize("ip,expected", [("1.1.1.1",
                                          {"city": None, "company": "Cloudflare", "continent_code": "OC",
                                           "country_code": "AU",
                                           "country_name": "Australia", "found": 1, "ip": "1.1.1.1",
                                           "ip_header": "IP address",
                                           "isp": "Cloudflare", "lat": -33.494, "lng": 143.2104, "metro_code": None,
                                           "postal_code": None, "region": None, "region_name": None,
                                           "time_zone": None}),
                                         ("8.8.8.8",
                                          {"city": None, "company": "Google", "continent_code": "NA",
                                           "country_code": "US", "country_name": "United States", "found": 1,
                                           "ip": "8.8.8.8", "ip_header": "IP address", "isp": "Google", "lat": 37.751,
                                           "lng": -97.822, "metro_code": None, "postal_code": None, "region": None,
                                           "region_name": None, "time_zone": None})])
def test_index(ip, expected):
    response = requests.get("{}/{}".format(TEST_HOST, ip))
    assert expected == response.json()["location"]
