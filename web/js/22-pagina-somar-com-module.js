// como este arquivo javascript utiliza import,
// é preciso que ele seja importado usando MODULE:
// <script type="module" src="./22-pagina-somar.js"></script>
import { PI, somar } from './23-biblioteca.js';

// colocando o valor na tela
document.getElementById('mostrar_pi').textContent = PI;

// somando números
const resultado = somar(5, 10);
document.getElementById('mostrar_soma').textContent = resultado;

// a função multiplicar foi importada por padrão
const mult = multiplicar(5, 10);
document.getElementById('mostrar_mult').textContent = mult;