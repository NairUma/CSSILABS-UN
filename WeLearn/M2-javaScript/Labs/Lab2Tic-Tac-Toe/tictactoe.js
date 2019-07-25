let p1 = [];
let p2 = [];
let playervalue=0;



const b1 = document.querySelector('#b1');
const b2 = document.querySelector('#b2');
const b3 = document.querySelector('#b3');
const b4 = document.querySelector('#b4');
const b5 = document.querySelector('#b5');
const b6 = document.querySelector('#b6');
const b7 = document.querySelector('#b7');
const b8 = document.querySelector('#b8');
const b9 = document.querySelector('#b9');


b1.addEventListener('click', (event) => {
  console.log("You clicked the 1 button!");
  if(playervalue%2===0){
      b1.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b1.style.backgroundColor = 'red';
    playervalue++;

  }

});

b2.addEventListener('click', (event) => {
  console.log("You clicked the 2 button!");
  if(playervalue%2===0){
      b2.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b2.style.backgroundColor = 'red';
    playervalue++;

  }

});

b3.addEventListener('click', (event) => {
  console.log("You clicked the 3 button!");
  if(playervalue%2===0){
      b3.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b3.style.backgroundColor = 'red';
    playervalue++;

  }


});

b4.addEventListener('click', (event) => {
  console.log("You clicked the 4 button!");
  if(playervalue%2===0){
      b4.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b4.style.backgroundColor = 'red';
    playervalue++;

  }

});

b5.addEventListener('click', (event) => {
  console.log("You clicked the 5 button!");
  if(playervalue%2===0){
      b5.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b5.style.backgroundColor = 'red';
    playervalue++;

  }

});

b6.addEventListener('click', (event) => {
  console.log("You clicked the 6 button!");
  if(playervalue%2===0){
      b6.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b6.style.backgroundColor = 'red';
    playervalue++;

  }

});

b7.addEventListener('click', (event) => {
  console.log("You clicked the 7 button!");
  if(playervalue%2===0){
      b7.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b7.style.backgroundColor = 'red';
    playervalue++;

  }

});

b8.addEventListener('click', (event) => {
  console.log("You clicked the 8 button!");
  if(playervalue%2===0){
      b8.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b8.style.backgroundColor = 'red';
    playervalue++;

  }

});

b9.addEventListener('click', (event) => {
  console.log("You clicked the 9 button!");
  if(playervalue%2===0){
      b9.style.backgroundColor = 'green';
      playervalue++;
  }
  else{
    b9.style.backgroundColor = 'red';
    playervalue++;

  }

});
