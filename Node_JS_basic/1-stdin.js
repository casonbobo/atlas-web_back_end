// create a program named 1-stdin.js that will be executed through command line

const readline = require('readline');

const prog = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

prog.question('Welcome to Holberton School, what is your name?', (name) => {
  console.log(`Your name is ${name}`);
  prog.close();
});

process.on('SIGINT', () => {
  console.log('This important software is now closing');
  process.exit();
});
