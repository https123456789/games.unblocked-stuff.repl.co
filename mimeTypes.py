# Mime Types
types = {
	"text/cache-manifest": [
		".appcache"
	],
	"text/plain": [
		".txt"
	],
	"application/json": [
		".json"
	],
	"text/javascript": [
		".js",
		".mjs"
	],
	"text/html": [
		".html",
		".htm"
	],
	"text/css": [
		".css"
	],
	"application/x-httpd-php": [
		".php"
	],
	"image/jpeg": [
		".jpg",
		".jpeg"
	],
	"image/png": [
		".png"
	],
	"audio/mpeg": [
		".mp3",
		".mpeg"
	],
	"video/mp4": [
		".mp4"
	],
	"image/svg+xml": [
		".svg"
	],
	"image/vnd.microsoft.icon": [
		".ico"
	],
	"application/octet-stream": [
		".bin"
	],
	"image/gif": [
		".gif"
	],
	"application/java-archive": [
		".jar"
	],
	"application/ogg": [
		".ogg"
	],
	"video/ogg": [
		".ogv"
	]
}

def getMimeTypeForExtension(filePath):
	fileName = filePath.split("/")[-1]
	if "." in fileName:
		fileExtension = "." + fileName.split(".")[-1]
	else:
		return "application/octet-stream"
	for ct in types.keys():
		if fileExtension in types[ct]:
			return ct
	return "application/octet-stream"