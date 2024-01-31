// Async function to fetch and display Star Wars movies
async function fetchAndDisplayMovies () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const { results } = await response.json();
    const moviesList = document.getElementById('list_movies');
    results.forEach(movie => {
      const movieItem = document.createElement('li');
      movieItem.textContent = movie.title;
      moviesList.appendChild(movieItem);
    });
  } catch (error) {
    console.error('Fetch error:', error);
  }
}
fetchAndDisplayMovies();
