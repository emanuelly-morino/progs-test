function somarComEspera(n1, n2) {
    return new Promise(
        (resolve) => {
            setTimeout(() => {
                resolve(n1 + n2);
            }, 1200);
        });
}

// valor inicial
let soma = 0;

// realizar 10 ações de sorteio e soma
for (let i = 0; i < 10; i++) {

    // sorteia um número entre 0 e 100
    let n = Math.random()
    n = parseInt(n * 100);

    // acrescenta o número sorteado na tela
    const element1 = document.getElementById("numero_sorteado");
    element1.textContent += `${n}, `;

    // soma o número sorteado com o valor inicial
    soma = await somarComEspera(n, soma);

    // mostra o resultado na tela
    const element = document.getElementById("soma");
    element.textContent = soma;
}