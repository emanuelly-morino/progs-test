import Image from "next/image";

export default async function Listar_Pessoas() {
  
  const response = await fetch('https://progs-3oir.onrender.com/pessoas');
  
  if (!response.ok) {
    throw new Error('Failed to fetch posts');
  }

  const lines = await response.json();

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <h1>Pessoas</h1>
        <ul>
          {lines.map((line: any) => (
            <li key={line.id}>{line.nome}</li>
          ))}
        </ul>
      </main>
    </div>
  );
}
