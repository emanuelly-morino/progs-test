
function sorteiaUmNumero() {
    return new Promise(
        (sorteia) => {
            setTimeout(() => {
                let n1 = Math.random();
                let n2 = n1 * 1000;
                let n3 = parseInt(n2);
                sorteia(n3);
            }, 1000);
        });
}

// locate the element on the screen
const element1 = document.getElementById("numbers");

for (let i = 0; i < 10; i++) {
    // get a random number
    let n = await sorteiaUmNumero();
    // put the number in the screen
    element1.textContent += `${n}, `;

}