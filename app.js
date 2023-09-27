const express = require("express");
const app = express();

const router = require('./routes/routes.js')

app.use(express.urlencoded({extended:false}));

app.set("view engine", "ejs");
app.set("views", "views");

app.use(router);

app.listen(8020, function() {
    console.log("Server lauscht auf http://localhost:8020");
});

const ejs = require('ejs');
app.engine('html', ejs.renderFile);
app.set('view engine', 'html');
