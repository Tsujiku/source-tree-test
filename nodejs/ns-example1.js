var http = require("http");

var server = http.createServer((req, res)=>{
    res.writeHead(200, {"Content-Type": "text/plane"});
    res.end("Hello Node.js\n");
});

server.listen(9000);

console.log("Server Running at http://127.0.0.1:9000/")