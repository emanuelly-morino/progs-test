// pages/dashboard.js
"use client";
import { useEffect, useState } from "react";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("jwt");
    if (!token) {
      setError("No token found. Please log in.");
      return;
    }

    fetch("http://localhost:5000/protected", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) setError(data.error);
        else setUser(data.user || data);
      })
      .catch(() => setError("Failed to fetch user data"));
  }, []);

  if (error) return <p className="text-red-500">{error}</p>;
  if (!user) return <p>Loading...</p>;

  return (
    <main className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-2xl font-bold mb-4">Welcome, {user.name}!</h1>
      <p>Email: {user.sub}</p>
      <button
        onClick={() => {
          localStorage.removeItem("jwt");
          window.location.href = "/";
        }}
        className="mt-4 px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700"
      >
        Logout
      </button>
    </main>
  );
}
