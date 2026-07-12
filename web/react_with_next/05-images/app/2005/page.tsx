import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
         <Link className="text-blue-500 hover:text-blue-700" href="/">Voltar</Link>
        <h1>2005</h1>
        Em 2005 morei até outubro nem Ilhéus, Bahia.
        Tempo de praia, muito trabalho e morando sozinho.
        <Image
          src="/DSC04057.JPG"
          alt="Morando na Bahia"
          width={1280}
          height={960}
          priority
        />
        
      
      </main>
    </div>
  );
}
