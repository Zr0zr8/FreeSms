import http.client
import json

conn = http.client.HTTPSConnection("e1zzvq.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"967775375736"}],
            "from": "ServiceSMS",
            "text": "Congratulations on sending your first message.\nGo ahead and check the delivery report in the next step."
        }
    ]
})
headers = {
    'Authorization': 'App 2d50d87a27c265dea8adfe0fe7c3172d-05d9323e-277d-475d-9e41-dc867493ba76',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
