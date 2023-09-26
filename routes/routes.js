const express = require("express");
const router = express.Router();

const persistence = require("../models/persistence.js");
router.use(express.static("public"));

router.get("/", function (req, res) {

  res.render("list", { PlacesArray : persistence.PlacesArray });
});

router.get("/SightseeingSpots", function (req, res) {

  if (req.query.place) {
    var place = persistence.getSightseeingtoPlace(req.query.place);
  } else {
    var Sightseeing = persistence.SightseeingArray;
  }
  res.render("SightseeingSpots", { Sightseeing : Sightseeing, place : req.query.place, getDauerInStundenUndMinuten : persistence.getDauerInStundenUndMinuten });
});

router.get("/Sightseeing", function (req, res) {

  const tutorial = persistence.SightseeingArray.find(t => t.name == req.query.name)
  res.render("Sightseeing", { Sightseeing : persistence.Sightseeing, getDauerInStundenUndMinuten : persistence.getDauerInStundenUndMinuten });
});

router.get("/CreateRecommendation", function (req, res) {

  res.render("CreateRecommendation");
});

router.post("/CreateRecommendation", function (req, res) {
 
  let places = req.body.places.split(',');
  for(let place of places) {
    let oldkat = persistence.PlacesArray.find(k => k.name == description);
    if (oldkat) {
      tutorial.fuegeOrtHinzu(oldkat);
    } else {
      let newkat = new persistence.Place(place, new persistence.picture( `https://img.icons8.com/${place.split(' ')[0].toLowerCase()}`, place));
      tutorial.fuegeOrtHinzu(newkat);
      persistence.PlacesArray.push(newkat);
    }
  }
  persistence.SightseeingArray.push(persistence.Place);
  console.log(persistence.Place);
  console.log(persistence.PlacesArray);
  res.redirect('http://localhost:8020/');
});

router.use(function (req, res) {
  res.status(404).render("error");
  
});

module.exports = router;