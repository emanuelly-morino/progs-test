export default async function Retornar_Pessoas() {

    const apiUrl = process.env.NEXT_PUBLIC_API_URL;

    let logs = "Página iniciada, buscando dados de: " + apiUrl + '/pessoas'

    // disable cache to get updated records!
    const response = await fetch(apiUrl + '/pessoas' , {cache: 'no-store'} ); 

    logs = logs + "; " + ' API disparada; ';

    //console.log('chamado: ' + apiUrl + '/pessoas');

    let lines = [];

    if (!response.ok) {
        //throw new Error("Failed to fetch posts");
        logs = logs + 'Erro ao buscar posts, response.ok = false';
    } else {

    const data = await response.json();

    logs = logs + "; " + ' respostas obtidas, resultado = ' + data?.resultado;

    lines = Array.isArray(data?.detalhes) ? data.detalhes : [];

    logs = logs + "; " + ' linhas obtidas = ' + lines.length;

    }
    return (
        <>
            {logs && (
                <p className="text-green-600 font-medium">
                    {logs}
                </p>
            )}

            <ul
                className="mt-6 w-full divide-y divide-gray-200 rounded-xl border border-gray-200 bg-white shadow-md"
            >
                {lines.map((line: { id: number; nome: string; email: string; telefone: string; login: string }) => (
                    <li key={line.id}
                        className="px-6 py-4 text-lg text-gray-800 transition-colors hover:bg-blue-50 hover:text-blue-700 cursor-pointer"
                    >{line.id}. {line.nome}, {line.email}, {line.telefone}, {line.login}</li>
                ))}
            </ul>
        </>
    );
}
