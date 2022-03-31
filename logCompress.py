import base64, json

file = open("server.log.json", "r")
data = json.dumps(json.load(file))
file.close()

baseData = base64.b64encode(bytes(data, "utf-8"))
baseData = baseData.decode("utf-8")

s = ""
i = 0
for ch in list(baseData):
	if i >= 50:
		s += "\n"
		i = 0
	s += ch
	i += 1

baseData = s

file = open("server.log.json.compressed", "w")
file.write(baseData)
file.close()