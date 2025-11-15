#!/usr/bin/node
const listMovies = document.querySelector('ul#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => console.error('error', error));
