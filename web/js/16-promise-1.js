function sorteiaUmNumero() {
    // cria um objeto do tipo Promise
    return new Promise(
        // a função sorteia é a função de callback que deve ser chamada quando o número for sorteado
        // o número sorteado deve ser passado como argumento para a função sorteia
        // essa função será chamada dentro do bloco da função com seta (Arrow Function)
        (sorteia) => {
            // é criado um temporizador
            setTimeout(
                // a função com seta é a função de callback que 
                // deve ser chamada quando o temporizador expirar
                () => {
                let n1 = Math.random();
                let n2 = n1 * 1000;
                let n3 = parseInt(n2);
                sorteia(n3);
            }, 
            // o temporizador é configurado 
            // para expirar após 1000 milissegundos (1 segundo)
            1000);
        });
}

// localiza o elemento na tela
const element1 = document.getElementById("numbers");

for (let i = 0; i < 10; i++) {
    // obtém um número aleatório
    // como a função sorteiaUmNumero retorna uma Promise, 
    // é necessário usar a palavra-chave await para 
    // esperar que a Promise seja resolvida e 
    // obter o número sorteado
    let n = await sorteiaUmNumero();
    // colocar o número sorteado na tela
    element1.textContent += `${n}, `;

}

