import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
         <Link className="text-blue-500 hover:text-blue-700" href="/">Voltar</Link>
        <h1>2006</h1>
        Em 2006 eu estava em Rio do Sul, caí de moto,
        trinquei a clavícula e aí fui passar em Santa Maria
        com meu amigo gaúcho.
        Posei ao lado do cavalo :-)
        <Image
          src="/DSC06400.JPG"
          alt="Ao lado do cavalo"
          width={1280}
          height={960}
          priority
        />
        
      
      </main>
    </div>
  );
}
