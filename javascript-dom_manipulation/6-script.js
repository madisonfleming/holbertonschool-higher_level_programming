const character = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Response not ok');
    }
  })
  .then((json) => {
    character.textContent = json.name;
  })
  .catch(error => console.error('error', error));
