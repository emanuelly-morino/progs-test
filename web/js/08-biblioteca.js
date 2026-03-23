// arquivo biblioteca.js

// itens exportados
export const PI = 3.14159;
export function somar(a, b) {
  return a + b;
}
// exportação “padrão” - deve haver somente 1 por módulo
export default function multiplicar(a, b) {
  return a * b;
}