let express = require("express");
let app = express();

const router = require(".routes.routes.js");

app.use(express.urlencoded({extended:false}));

app.set("views-engine", "ejs")
app.set("views", "views")

app.use(router);

app.listen(3000, '172.225.195.65', function() {
    console.log('Listening to port:  ' + 3000);
});