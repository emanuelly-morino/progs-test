export default function Home() {
  // este componente é executado no servidor
  // por exemplo, no console.log abaixo, 
  // a mensagem aparecerá no terminal do npm run dev, 
  // e não no console do navegador
  // verifique quando executar este projeto :-)
  console.log("Esta mensagem aparece no terminal do servidor");
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        
        <h1 className="text-6xl font-bold tracking-tight text-center text-gray-900 dark:text-white sm:text-left">
          Bem vindo ao NextJS!
        </h1>
        <a href="/about"> Sobre </a>
        <a href="/about"> História </a>

      </main>
    </div>
  );
}
