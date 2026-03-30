async function carregarPosts() {
  // busca posts do backend
  const response = await fetch('/posts');
  // converte resposta para JSON
  const posts = await response.json();

  // limpa lista atual
  const lista = document.getElementById('lista-posts');
  lista.innerHTML = '';

  // percorre cada post da lista de posts
  posts.forEach(post => {
    // cria um elemento de lista
    const li = document.createElement('li');
    // preenche o conteúdo 
    li.innerHTML = `<strong>${post.titulo}</strong>: ${post.conteudo}`;
    // adiciona o elemento na lista HTML
    lista.appendChild(li);
  });
}

async function criarPost() {
  // pega os valores digitados
  const titulo = document.getElementById('titulo').value;
  const conteudo = document.getElementById('conteudo').value;

  // prepara o conteúdo da requisição
  // converte o objeto JavaScript para uma string JSON
  const dados = JSON.stringify({ titulo, conteudo });
  alert(`enviando para o backend: ${dados}`);
    
  // envia para o backend
  await fetch('/posts', {
    method: 'POST',
    headers: {
      // sinaliza que os dados estão sendo enviados em formato JSON
      'Content-Type': 'application/json'
    },
    body: dados
  });

  // limpa campos
  document.getElementById('titulo').value = '';
  document.getElementById('conteudo').value = '';

  // carrega novamente os post
  // para mostrar o post recém criado
  carregarPosts();
}

// carrega posts ao abrir
carregarPosts();