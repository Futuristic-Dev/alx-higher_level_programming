// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// The title must be displayed in the HTML tag UL#list_movies

$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (const movie of data.results) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  });
});