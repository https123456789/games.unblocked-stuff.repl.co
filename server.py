# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os, datetime, json, importlib, requests
import mimeTypes

hostName = "0.0.0.0"
serverPort = 8080

logCount = 0

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		global logCount
		logCount += 1
		if (logCount >= 100):
			os.system("clear && python logCompress.py")
			logCount = 0
		# Mime Types
		importlib.reload(mimeTypes)
		
		req = self.path.split("?")
		self.path = self.path.split("?")[0]
		#print(self.path[-1], end=" - ")
		if self.path[-1] == "/":
			self.path += "index.html"
		print(self.path + ": " + str(self.client_address[0]), end = "\n\tContent-Type: ")
		try:
			file = open(os.getcwd() + self.path, "rb")

			contentType = mimeTypes.getMimeTypeForExtension(self.path)
			print(contentType, end="\n\tStatus: ")
			self.send_response(200)
			print("200", end="")
			self.send_header("Access-Control-Allow-Origin", "*")
			if (contentType):
				self.send_header("Content-Type", contentType)
			self.end_headers()
			self.wfile.write(file.read())
			file = open("server.log.json", "r")
			try:
				data = json.load(file)
			except json.decoder.JSONDecodeError:
				print("\033[31mJSONDecodeError\033[0m")
				return
			file.close()
			try:
				data["stats"]
			except KeyError:
				data["stats"] = {}
			try:
				data["stats"][self.path] += 1
			except KeyError:
				data["stats"][self.path] = 1
			file = open("server.log.json", "w")
			file.write(json.dumps(data))
			file.close()
			upr = requests.post("https://admin.unblocked-stuff.repl.co/updatedb.php", data = json.dumps(data));
		except FileNotFoundError:
			self.send_response(404)
			print("404", end="")
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()
			file = open("404", "rb")
			self.wfile.write(file.read())
		except IsADirectoryError:
			self.send_response(404)
			print("404", end="")
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()
			file = open("404", "rb")
			self.wfile.write(file.read())
		print("")
	def log_message(self, format, *args):
		file = open("server.log.json", "r")
		try:
			data = json.load(file)
		except json.decoder.JSONDecodeError:
			print("\033[31mJSONDecodeError\033[0m")
			return
		file.close()
		self.client_address = list(self.client_address)
		self.client_address.pop()
		if len(data["requests"]) > 10:
			del data["requests"][-1]
		data["requests"].reverse()
		data["requests"].append({
			"date": str((datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S")),
			"path": str(self.path),
			"clientIPAddresses": list(self.client_address)
		})
		data["requests"].reverse()
		file = open("server.log.json", "w")
		file.write(json.dumps(data))
		file.close()
		return

if __name__ == "__main__":
	webServer = HTTPServer((hostName, serverPort), MyServer)
	print("Server started http://%s:%s" % (hostName, serverPort))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	print("Server stopped.")