var express = require("express");
var router = express.Router();
var googleFinance = require("google-finance");

router.get("/:stock", (req, res, next) => {
   googleFinance.historical({
       symbol: "IIJ:" + req.params.stock
   }, function(err, quotes) {
       if (err) {
           console.log(err);
           res.json({"msg": err});
       } else {
           var data_close = [];
           for(var i = 0; i < quotes.length; i++) {
               data_close.push(quotes[i].close);
           }
           res.json(data_close);
       }
   }) 
});

module.exports = router;