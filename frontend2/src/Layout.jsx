import React from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function AppLayout({ children }) {
  const location = useLocation();
  
  return (
    <div className="flex h-screen bg-gray-900 text-white overflow-hidden">
      <div className="w-64 bg-gray-800 flex flex-col flex-shrink-0">
        <div className="p-6 text-xl font-bold border-b border-gray-700 text-center text-blue-400">
          Agent PF
        </div>
        <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
          <Link
            to="/"
            className={`block p-3 rounded-lg transition-colors ${
              location.pathname === '/' ? 'bg-blue-600' : 'hover:bg-gray-700'
            }`}
          >
            💬 Chat
          </Link>
          <Link
            to="/state-util"
            className={`block p-3 rounded-lg transition-colors ${
              location.pathname === '/state-util' ? 'bg-blue-600' : 'hover:bg-gray-700'
            }`}
          >
            📋 Respostas
          </Link>
        </nav>
      </div>

      <main className="flex-1 flex flex-col overflow-hidden relative bg-gray-900">
        {children}
      </main>
    </div>
  );
}
