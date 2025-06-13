import FileUploader from './components/FileUploader'
import ChatWindow from './components/ChatWindow.jsx'

function App() {
  return (
    <div style={{ padding: 20 }}>
      <h1>🤖 AI Document Assistant</h1>
      <FileUploader />
      <ChatWindow />
    </div>
  )
}

export default App
