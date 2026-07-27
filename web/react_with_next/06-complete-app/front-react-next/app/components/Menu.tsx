// components/Menu.tsx

import Link from "next/link";

export default function Menu() {
  return (
    <nav className="bg-blue-600 text-white p-4">
      <ul className="flex gap-6">
        <li><Link href="/">Home</Link></li>
        <li><Link href="/listar_pessoas">Listar pessoas</Link></li>
        <li><Link href="/form_login">Login</Link></li>
        <li><Link href="/form_incluir_pessoa">Nova Pessoa</Link></li>
      </ul>
    </nav>
  );
}