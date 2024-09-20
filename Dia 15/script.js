const textarea=document.querySelector('textarea');
const count=document.querySelector('.count');

function contar(){
    const texto=textarea.value;
    const textlenght = textarea.value.length;

    count.innerText=`${textlenght}`;
}
