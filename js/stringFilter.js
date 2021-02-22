
const example = "01 clip[2]"
let nome, qtd;
  console.log(example)

for (let i=0; i<example.length; i++) {
  let a = example.charAt(i);

  if((isNaN(a))||(i > 4)||(a === " ")){
		nome = nome + a;
  } else {
  	qtd = qtd + a;
  }        



}

console.log("item :" + nome);
console.log("quantidade :" + qtd);