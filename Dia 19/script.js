const API = 'e58bfd93a525a2df533b989eb459293d';

function dadosNaTela(dados){
    document.querySelector(".cidade").innerHTML ="Tempo em " + dados.name;
    document.querySelector(".temp").innerHTML = Math.floor(dados.main.temp) +" Graus";
    document.querySelector(".texto-previsao").innerHTML = dados.weather[0].description;
    document.querySelector(".cidade").innerHTML = "Umidade: " +dados.main.umidity + "%";
    document.querySelector("img-previsão").src=`https://openweathermap.org/1mg/wn/${dados.weather[0].icon}.png`
}

async function buscarCidade(cidade) {
    const dados=await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${API}&lang=pt_br&units-metric`).then(resposta => resposta.json);
    dadosNaTela(dados);
}

function clickButton(){
    const cidade = document.querySelector(".input-cidade").value;

    buscarCidade(cidade);
}