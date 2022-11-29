import { map, getBounds, addMarkers } from './map.js';

const getIndividualData = individual => {
  $.ajax({
    type: "GET",
    url: "api/get-individual",
    data: {individual: individual},
    dataType: "JSON",
    success: function (response) {
      const individualsData = JSON.parse(response.data);
      const location = response.location;
      const boundingBox = response.bounding_box;
      const flights = response.flights;
      map.fitBounds(getBounds(location));
      addMarkers(individualsData, boundingBox, flights, map);
      displayFlights(response.n_flights);
      displayObservations(response.n_tracks);
    }
  });
};

const showSelectedIndividual = (individual) => {
  $(".selected-individual").html(`Individual ${individual}`);
};

const displayObservations = (observations) => {
  $(".n-observations").html(`${observations} tracks`);
}

const displayFlights = (flights) => {
  $(".n-flights").html(`${flights} flights`);
}

export const initializeIndividuals = () => {
  $(document).ready( () => {
    $(".individual-item").click( ev => {
      const individual = ev.target.dataset.individual;
      getIndividualData(individual);
      showSelectedIndividual(individual);
    })
  });
};
