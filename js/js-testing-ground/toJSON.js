
let string = readLine();

string = string.split(" ");

string = JSON.stringify(string.filter(item => item));

console.log(string);