# IP Locator API

> Lambda based application to locate information about any public IP address

### Getting started

Start the API locally

```shell script
$ pip install -r ./requirements.txt
$ chalice local
Serving on http://127.0.0.1:8000
```

Make a request

```shell script
$ curl -s http://127.0.0.1:8000/1.1.1.1 | jq
{
  "message": "success",
  "location": {
    "city": null,
    "company": "Cloudflare",
    "continent_code": "OC",
    "country_code": "AU",
    "country_name": "Australia",
    "found": 1,
    "ip": "1.1.1.1",
    "ip_header": "IP address",
    "isp": "Cloudflare",
    "lat": -33.494,
    "lng": 143.2104,
    "metro_code": null,
    "postal_code": null,
    "region": null,
    "region_name": null,
    "time_zone": null
  }
}
```

### Deploying to AWS Lambda

```shell script
$ chalice deploy
Creating deployment package.
Updating policy for IAM role: ip-locator-dev
Updating lambda function: ip-locator-dev
Updating rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:eu-west-1:00000000000:function:ip-locator-dev
  - Rest API URL: https://example.execute-api.eu-west-1.amazonaws.com/api/
```

Yor application is fully deployed, you can use the Rest API URL to make your requests


### Roadmap

- ~~Initial version~~
- Fallback providers
- Use a common schema between providers

### License

MIT