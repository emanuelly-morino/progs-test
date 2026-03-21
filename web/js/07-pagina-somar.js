import multiplicar, { PI, somar } from './08-biblioteca.js';

window.PI = PI;
window.somar = somar;
window.multiplicar = multiplicar;

// colocando o valor na tela
document.getElementById('mostrar_pi').textContent = PI;

// somando números
const resultado = somar(5, 10);
document.getElementById('mostrar_soma').textContent = resultado;

// a função multiplicar foi importada por padrão
const mult = multiplicar(5, 10);
document.getElementById('mostrar_mult').textContent = mult;