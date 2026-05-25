// o componente precisa ficar dentro de uma função
function Post() {
    // a função precisa retornar um código HTML
    return (
        <div>
            <h1>Olá este é um post</h1>
        </div>
    );
}

// deixando o componente apto para ser usado
// externamente, ou seja, em outros arquivos
export default Post;