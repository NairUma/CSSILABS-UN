 /*
const names = ['Alice', 'Bob', 'Charlie', 'Deborah', 'Evan'];

console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
console.log(names[3]);
console.log(names[4]);

for (let i = 0; i < 5; i++) {
  console.log(names[i]);
}

const books = ['Ari & Dante', 'An Enchantment of Ravens', 'The Tethered Mage',
'These Witches Dont Burn', 'Stuff Matters'];
books.forEach((book) => {
  console.log(book);
})

let sum = 0;
let numbers = [1,2,3,4,5,6,7,8,9,10];

const findTotal = ((item) => {
  sum = sum + item;
  console.log(sum);
});
*/

const button = document.querySelectorAll('button');
const box = document.querySelectorAll('#box');

button.forEach((button) => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
