var express = require("express");
var googleFinance = require("google-finance");
var bodyParser = require("body-parser");
var cors = require("cors");
var app = express();
var router = require("./router/route");

const port = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use("/saham", router);
app.listen(port, ()=>{
    console.log("server start at port 3000");
});

