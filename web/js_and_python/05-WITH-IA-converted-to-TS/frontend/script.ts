interface Filme {
  id?: number;
  nome: string;
  ano: number;
  categoria: string;
  classificacao: number;
}

const API_URL: string = "http://127.0.0.1:5000/filmes";

const filmeForm = document.getElementById("filmeForm") as HTMLFormElement;
const filmesLista = document.getElementById("filmesLista") as HTMLDivElement;

const filmeId = document.getElementById("filmeId") as HTMLInputElement;
const nomeInput = document.getElementById("nome") as HTMLInputElement;
const anoInput = document.getElementById("ano") as HTMLInputElement;
const categoriaInput = document.getElementById("categoria") as HTMLInputElement;
const classificacaoInput = document.getElementById("classificacao") as HTMLInputElement;

const cancelarBtn = document.getElementById("cancelarBtn") as HTMLButtonElement;

document.addEventListener("DOMContentLoaded", () => {
  listarFilmes();
});

filmeForm.addEventListener("submit", async (event: SubmitEvent) => {
  event.preventDefault();

  const filme: Filme = {
    nome: nomeInput.value,
    ano: Number(anoInput.value),
    categoria: categoriaInput.value,
    classificacao: Number(classificacaoInput.value)
  };

  if (filmeId.value) {
    await atualizarFilme(Number(filmeId.value), filme);
  } else {
    await criarFilme(filme);
  }

  limparFormulario();
  listarFilmes();
});

cancelarBtn.addEventListener("click", () => {
  limparFormulario();
});

async function listarFilmes(): Promise<void> {
  try {
    const response: Response = await fetch(API_URL);

    const filmes: Filme[] = await response.json();

    filmesLista.innerHTML = "";

    filmes.forEach((filme: Filme) => {
      const card = document.createElement("div");

      card.className = "filme-card";

      card.innerHTML = `
        <strong>${filme.nome}</strong> (${filme.ano})<br>
        Categoria: ${filme.categoria}<br>
        Classificação: ${filme.classificacao}

        <div class="actions">
          <button class="editar-btn">Editar</button>
          <button class="deletar-btn">Excluir</button>
        </div>
      `;

      const editarBtn = card.querySelector(".editar-btn") as HTMLButtonElement;
      const deletarBtn = card.querySelector(".deletar-btn") as HTMLButtonElement;

      editarBtn.addEventListener("click", () => editarFilme(filme));

      deletarBtn.addEventListener("click", async () => {
        if (filme.id) {
          await deletarFilme(filme.id);
        }
      });

      filmesLista.appendChild(card);
    });

  } catch (error) {
    console.error("Erro ao listar filmes:", error);
  }
}

async function criarFilme(filme: Filme): Promise<void> {
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

async function atualizarFilme(id: number, filme: Filme): Promise<void> {
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

async function deletarFilme(id: number): Promise<void> {
  const confirmar: boolean = confirm("Deseja excluir este filme?");

  if (!confirmar) return;

  try {
    await fetch(`${API_URL}/${id}`, {
      method: "DELETE"
    });

    listarFilmes();

  } catch (error) {
    console.error("Erro ao deletar filme:", error);
  }
}

function editarFilme(filme: Filme): void {
  filmeId.value = filme.id?.toString() || "";

  nomeInput.value = filme.nome;
  anoInput.value = filme.ano.toString();
  categoriaInput.value = filme.categoria;
  classificacaoInput.value = filme.classificacao.toString();
}

function limparFormulario(): void {
  filmeForm.reset();
  filmeId.value = "";
}