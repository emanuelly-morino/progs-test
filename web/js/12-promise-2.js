function retornoComEspera(n) {
    return new Promise(
        (sorteia) => {
            setTimeout(() => {
                sorteia(n);
            }, 2000);
        });
}

let n1 = await retornoComEspera(5);
const element1 = document.getElementById("n1");
element1.textContent = n1;

let n2 = await retornoComEspera(5);
const element2 = document.getElementById("n2");
element2.textContent = n2;

let soma = n1 + n2;
const element3 = document.getElementById("soma");
element3.textContent = soma;
