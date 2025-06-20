import './App.css'
import FileUploader from './components/FileUploader'
import ChatWindow from './components/ChatWindow'
import { useState } from 'react'

function App() {
  const [chatResponse, setChatResponse] = useState("")

  return (
    <div className="app-container">
      <header className="app-header">
        <span className="app-logo">🤖</span>
        <h1 className="app-title">AI Document Assistant</h1>
      </header>

      <main className="app-grid">
        <div className="left-panel">
          <section className="app-section">
            <FileUploader />
          </section>
          <section className="app-section">
            <ChatWindow setResponse={setChatResponse} />
          </section>
        </div>

        <div className="right-panel">
          <section className="response-viewer">
            <h3>📄 Answer</h3>
            <p>{chatResponse ? chatResponse : "Start chatting and see the insights unfold!"}</p>
          </section>
        </div>
      </main>

      <footer className="app-footer">
        <p>© 2025 - AI Document Assistant</p>
      </footer>
    </div>
  )
}

export default App
