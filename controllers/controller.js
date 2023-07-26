const data = require("../models/data");
const login = require("../views/login");

module.exports.showlogin = function(req, res) {
    res.send(login());
};

module.exports.main = function(req, res) {
    res.send(main());
};

module.exports.planning = function(req, res) {
    res.send(planning());
};

module.exports.showregistration = function(req, res) {
    res.send(registration());
};