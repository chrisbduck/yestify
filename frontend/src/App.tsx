import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function ApiContent({ endpoint, name, children }: { endpoint: string, name: string, children?: React.ReactNode }) {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    fetch(`/api/${endpoint}?name=${name}`)
      .then((r) => r.json())
      .then((j) => setMsg(j.message))
      .catch((e) => setMsg(String(e)));
  }, [endpoint, name]);

  return (
    <div style={{ padding: 24 }}>
      <h1>{msg}</h1>
      {children}
    </div>
  );
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <ApiContent endpoint="hello" name="Chris">
        <p>React + Vite frontend, Python (FastAPI) serverless backend on Vercel.</p>
      </ApiContent>
      <ApiContent endpoint="goodbye" name="Chris" />
    </>
  )
}

export default App
