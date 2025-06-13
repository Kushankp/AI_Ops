import { useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState("")
  const [response, setResponse] = useState("")

  const sendMessage = async () => {
    try {
      const res = await axios.post('http://localhost:8000/chat', { message })
      setResponse(res.data.reply)
    } catch (err) {
      console.error("Error:", err)
      setResponse("Something went wrong.")
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>💬 LLM Agent Chat</h2>
      <textarea
        rows="4"
        cols="50"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <button onClick={sendMessage}>Send</button>
      <p><strong>Agent:</strong> {response}</p>
    </div>
  )
}

export default App
