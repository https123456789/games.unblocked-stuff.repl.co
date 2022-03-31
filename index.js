const http = require('http');
const fs = require("fs");

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  	res.statusCode = 200;
  	res.setHeader('Content-Type', 'text/plain');
	var path = "." + req.url;
	var psplit = path.split("/");
	console.log(psplit);
	if (psplit.at(-1) == "") {
		path += "index.html";
	}
	console.log(path);
	try {
		fs.readFile(path, (err, data) => {
			if (err) {
				console.error(err);
				res.end(err);
			}
	  		res.end(data);
		});
	} catch (err) {
		console.error(err);
		res.end(err);
	}
});

server.listen(port, hostname, () => {
  	console.log(`Server running at http://${hostname}:${port}/`);
});