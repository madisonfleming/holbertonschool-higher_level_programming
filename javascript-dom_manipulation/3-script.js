const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', () => {
  if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
});
