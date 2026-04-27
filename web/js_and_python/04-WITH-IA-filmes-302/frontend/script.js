const API_URL = "http://10.10.34.39:5000/filmes";

const filmeForm = document.getElementById("filmeForm");
const filmesLista = document.getElementById("filmesLista");

document.addEventListener("DOMContentLoaded", listarFilmes);

filmeForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("filmeId").value;

    const filme = {
        nome: document.getElementById("nome").value,
        ano: parseInt(document.getElementById("ano").value),
        categoria: document.getElementById("categoria").value,
        classificacao: parseInt(document.getElementById("classificacao").value),
    };

    if (id) {
        await atualizarFilme(id, filme);
    } else {
        await criarFilme(filme);
    }

    limparFormulario();
    listarFilmes();
});

async function listarFilmes() {
    try {
        const response = await fetch(API_URL);
        const filmes = await response.json();

        filmesLista.innerHTML = "";

        filmes.forEach(filme => {
            filmesLista.innerHTML += `
                <div class="filme-card">
                    <strong>${filme.nome}</strong> (${filme.ano})<br>
                    Categoria: ${filme.categoria}<br>
                    Classificação: ${filme.classificacao}
                    <div class="actions">
                        <button onclick='editarFilme(${JSON.stringify(filme)})'>Editar</button>
                        <button onclick='deletarFilme(${filme.id})'>Excluir</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        console.error("Erro ao listar filmes:", error);
    }
}

async function criarFilme(filme) {
    try {
        await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(filme)
        });
    } catch (error) {
        console.error("Erro ao criar filme:", error);
    }
}

async function atualizarFilme(id, filme) {
    try {
        await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(filme)
        });
    } catch (error) {
        console.error("Erro ao atualizar filme:", error);
    }
}

async function deletarFilme(id) {
    if (!confirm("Deseja realmente excluir este filme?")) return;

    try {
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        listarFilmes();
    } catch (error) {
        console.error("Erro ao deletar filme:", error);
    }
}

function editarFilme(filme) {
    document.getElementById("filmeId").value = filme.id;
    document.getElementById("nome").value = filme.nome;
    document.getElementById("ano").value = filme.ano;
    document.getElementById("categoria").value = filme.categoria;
    document.getElementById("classificacao").value = filme.classificacao;
}

function limparFormulario() {
    filmeForm.reset();
    document.getElementById("filmeId").value = "";
}