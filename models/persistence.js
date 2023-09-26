class SightseeingSpots
{
    constructor(name, picture)
    {
      this.name = name;
      this.picture = picture;
    }
}

class Sightseeing
{
    constructor(name, language, description, duration, date, picture)
    {
      this.name = name;
      this.langugage = language;
      this.description = description;
      this.duration = duration;
      this.date = date;
      this.picture = picture;
      this.places = [];
      this.placesList = [];
    }

    fuegeOrtHinzu(kat)
    {
      this.places.push(kat);
    }
  
    fuegeOrtHinzu(kap)
    {
      this.placesList.push(kap);
    }
}

class Picture 
{
    constructor(url, name)
    {
      this.url = url;
      this.name = name;
    }
}
  
class Place
{
    constructor(name, description, weather)
    {
      this.name = name;
      this.description = description;
      this.weather = weather;
    }
}

function getDauerInStundenUndMinuten(duration)
{
    let time = duration.split(':');
    if(time[0] != '00')
    {
        return `${time[0]} Std. ${time[1]} Min.`;
    }
    return `${time[1]} Min.`;    
}

const Place1 = new Place
(
    "Hot",
    new Picture("img/desert.jpeg", "Hot places")
);

const Place2 = new Place
(
    "Cold",
    new Picture("img/cold.jpeg", "Cold places")
);

const Place3 = new Place
(
    "City",
    new Picture("img/City.jpeg", "Cities")
);

const Place4 = new Place
(
    "Nature",
    new Picture("img/nature.jpeg", "Nature")
);

const Sightseeing1 = new Sightseeing
(
    "Turkey",
    "english",
    "Get your guide for a desert",
    "8:00",
    new Date(),
    new Picture("img/desert.jpeg", "Picture of Turkey")
);

const Sightseeing2 = new Sightseeing
(
    "Norway",
    "english",
    "get your guide for a snow world",
    "04:40",
    new Date(),
    new Picture("img/snow.jpeg", "Picture of norway")
);

Sightseeing1.fuegeOrtHinzu(Place1);
Sightseeing1.fuegeOrtHinzu(Place3);

Sightseeing2.fuegeOrtHinzu(Place1);
Sightseeing2.fuegeOrtHinzu(Place3);

Sightseeing1.fuegeOrtHinzu(Place1);
Sightseeing1.fuegeOrtHinzu(Place2);
Sightseeing1.fuegeOrtHinzu(Place3);
Sightseeing1.fuegeOrtHinzu(Place4);

const PlacesArray = [Place1, Place2, Place3, Place4];

const SightseeingArray = [Sightseeing1, Sightseeing2];

SightseeingArray.sort((a, b) => a.name.localeCompare(b.name));

function getSightseeingtoPlace(PlacesName)
{
    return SightseeingArray.filter(t => t.Orte.find(k => k.name == PlacesName));
}
  
module.exports.PlacesArray = PlacesArray;
module.exports.SightseeingArray = SightseeingArray;
module.exports.getDauerInStundenUndMinuten = getDauerInStundenUndMinuten;
module.exports.getSightseeingtoPlace = getSightseeingtoPlace;
module.exports.Sightseeing = Sightseeing;
module.exports.Picture = Picture;
module.exports.Place = Place;