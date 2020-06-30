import logging
import requests
from chalice import Chalice, CORSConfig, Response

app = Chalice(app_name='ip-locator')

cors_config = CORSConfig(
    allow_origin='*',
    allow_headers=[],
    max_age=600,
    expose_headers=[],
    allow_credentials=False
)


@app.route('/{ip}', methods=["GET"], cors=cors_config)
def index(ip):
    app.log.debug("Looking for IP {}".format(ip))
    response = requests.post("https://iplocation.com/", data={"ip": ip})
    if response.ok:
        app.log.debug("Found information for IP {}: {}".format(ip, response.json()))
        return Response(body={"message": "success", "location": response.json()}, status_code=200)
    app.log.debug("No information found for IP {}: {}".format(ip, response.json()))
    return Response(body={"message": "nothing found"}, status_code=400)
