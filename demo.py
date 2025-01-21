import httpx, json

deeplx_api = "http://node-kyb.bariskeser.com:1188/translate"

data = {
	"text": "Hello World",
	"source_lang": "EN",
	"target_lang": "TR"
}

post_data = json.dumps(data)
r = httpx.post(url = deeplx_api, data = post_data)
print(r)