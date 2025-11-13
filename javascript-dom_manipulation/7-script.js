#!/usr/bin/node

const listMovies = document.querySelector('ul.list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Response not ok');
    }
  })
  .then((json) => {
    listMovies.appendChild(json.title);
  })
  .catch(error => console.error('error', error));
