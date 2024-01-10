$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus, jqXHR) {
    $.each(data.results, function (index, value) {
      $('UL#list_movies').append(`<li>${value.title}</li>`);
    });
  }
);
