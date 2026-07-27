export default async function Listar_Pessoas() {

  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  const response = await fetch(apiUrl+'/pessoas');

  console.log('chamado: '+apiUrl+'/pessoas');

  if (!response.ok) {
    throw new Error("Failed to fetch posts");
  }

  const data = await response.json();
  const lines = Array.isArray(data?.detalhes) ? data.detalhes : [];  

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <h1
        className="text-4xl font-bold tracking-tight text-gray-900 mb-4"
        >Pessoas</h1>
        <ul
        className="mt-6 w-full divide-y divide-gray-200 rounded-xl border border-gray-200 bg-white shadow-md"
        >
          {lines.map((line: { id: number; nome: string; email: string; telefone: string; login: string }) => (
            <li key={line.id}
            className="px-6 py-4 text-lg text-gray-800 transition-colors hover:bg-blue-50 hover:text-blue-700 cursor-pointer"
            >{line.id}. {line.nome}, {line.email}, {line.telefone}, {line.login}</li>
          ))}
        </ul>
      </main>
    </div>
  );
}
