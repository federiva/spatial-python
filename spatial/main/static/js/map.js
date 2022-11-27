export let map = L.map('map-flights').setView([51.505, -0.09], 13);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let markers = L.layerGroup([]);
export const getBounds = location => {
  return [[location.min_lat, location.min_lon], [location.max_lat, location.max_lon]]
};

export const addMarkers = (data, map) => {
  markers.clearLayers();
  data.map( individual => {
    const lat = individual.fields.location_lat;
    const lon = individual.fields.location_long;
    const marker = L.marker([lat, lon])
    markers.addLayer(marker);
  })
  markers.addTo(map);
};
