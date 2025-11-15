#!/usr/bin/node
window.onload = function () {
  const hello = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then((json) => {
      hello.textContent = json.hello;
    })
    .catch(error => console.error('error', error));
};
