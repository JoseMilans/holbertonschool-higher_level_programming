const header = document.querySelector('header');
const updateHeaderButton = document.getElementById('update_header');
updateHeaderButton.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
