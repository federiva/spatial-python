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
      map.fitBounds(getBounds(location));
      addMarkers(individualsData, map);
    }
  });
};

export const initializeIndividuals = () => {
  $(document).ready( () => {
    $(".individual-item").click( ev => {
      const individual = ev.target.dataset.individual;
      getIndividualData(individual);
    })
  });
};
