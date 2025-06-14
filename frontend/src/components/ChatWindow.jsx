import { useState } from 'react'
import axios from 'axios'

function ChatWindow() {
  const [message, setMessage] = useState("")
  const [response, setResponse] = useState("")
  const [loading, setLoading] = useState(false)

  const sendMessage = async () => {
    if (!message.trim()) return

    setLoading(true)
    try {
      const res = await axios.post("https://c92a5e29-ef5c-4e14-b72f-7fc2b227cc1b-00-3mc63l854b256.pike.replit.dev/chat", { message })
      setResponse(res.data.reply)
    } catch (err) {
      console.error("Error:", err)
      setResponse("Something went wrong.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ marginTop: 40 }}>
      <h2>💬 Ask a Question</h2>
      <textarea
        rows="4"
        cols="50"
        placeholder="Ask something about the uploaded document..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <button onClick={sendMessage} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>
      <p><strong>Answer:</strong> {response}</p>
    </div>
  )
}

export default ChatWindow
