import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        
        Página do Hylson

        <Link className="text-blue-500 hover:text-blue-700" href="/2005">2005 - Bahia</Link>
        <Link className="text-blue-500 hover:text-blue-700" href="/2006">2006 - Rio do Sul</Link>
        <Link className="text-blue-500 hover:text-blue-700" href="/2008">2008 - Cozinhando e viajando</Link>


        
      
      </main>
    </div>
  );
}
