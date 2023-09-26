const http = require("http");
const url = require("url");
const persistence = require("./models/persistence.js");

const server = http.createServer(function(req, res) {
    const queryParams = url.parse(req.url, true).query;
    const html = generiereHtmlFuerSuchergebnisse(persistence.SightseeingArray.filter(t => t.name.match(new RegExp(queryParams.search, "g"))), queryParams.search);
    res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
    res.end(html);
});

server.listen(8844, function() {
    console.log("Ich lausche auf http://localhost:8844");
});