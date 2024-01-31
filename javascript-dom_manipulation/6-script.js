const characterElement = document.getElementById('character');
async function fetchAndDisplayCharacterName () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    const data = await response.json();
    characterElement.textContent = data.name;
  } catch (error) {
    console.error('Fetch error:', error);
  }
}
fetchAndDisplayCharacterName();
