const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');
addItemButton.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  myList.appendChild(newLi);
});
