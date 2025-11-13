#!/usr/bin/node
const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', () => {
  header.style.backgroundColor = '#FF0000';
});
