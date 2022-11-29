export let map = L.map('map-flights').setView([51.505, -0.09], 13);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let markers = L.layerGroup([]);
export const getBounds = location => {
  return [[location.min_lat, location.min_lon], [location.max_lat, location.max_lon]]
};

const planeIcon = L.icon({
  
  iconUrl: 'https://cdn.iconscout.com/icon/free/png-256/plane-150-450597.png',
  iconSize: [38, 95],
  iconAnchor: [22, 94],
  popupAnchor: [-3, -76],
  shadowSize: [68, 95],
  shadowAnchor: [22, 94],
});
console.log(planeIcon)

export const addMarkers = (data, boundingBox, flights, map) => {
  markers.clearLayers();
  let points = [];
  const boundLayer = L.rectangle(boundingBox, {color: "#ff7800", weight: 1})
  data.map( individual => {
    const lat = individual.fields.location_lat;
    const lon = individual.fields.location_long;
    const marker = L.marker([lat, lon])
    points.push([lon, lat])
    markers.addLayer(marker);
  })
  if (!!flights) {
    flights.map( flight => {
      console.log(flight)
      window.flight = flight;
      const lat = flight[0][0];
      const lon = flight[0][1];
      const marker = L.marker([lat, lon], {icon: planeIcon, opacity: 0.8})
      points.push([lon, lat])
      markers.addLayer(marker);
    })
  }
  
  markers.addLayer(boundLayer);
  markers.addTo(map);
};
