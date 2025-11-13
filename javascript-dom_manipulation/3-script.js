#!/usr/bin/node
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', () => {
  header.classList.toggle('red');
  header.classList.toggle('green');
});
