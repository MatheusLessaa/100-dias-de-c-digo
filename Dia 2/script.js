let user1 = prompt ("Digite o primeiro número de usuário");  //Pergunta no navegador o primeiro usuário
let user2 = prompt ("Digite o segundo número de usuário");  //Pergunta no navegador o segundo usuário

user1 = parseFloat(user1);  //transforma o valor do primeiro usuário em numérico (até então era indefinido)
user2 = parseFloat(user2);  //transforma o valor do segundo usuário em numérico (até então era indefinido)

let soma = user1+user2; //soma o valor dos dois usuários e guarda o resultado na variável "soma"
alert("Resultado da soma: "+soma); //Alerta na tela o valor da variável "soma"
console.log("Resultado da soma: ", soma); //imprime no console o valor da variável "soma"