import { useState } from 'react'
import axios from 'axios'
import '../App.css'

function ChatWindow({ setResponse }) {
  const [message, setMessage] = useState("")
  const [loading, setLoading] = useState(false)

  const sendMessage = async () => {
    if (!message.trim()) return
    setLoading(true)
    try {
      const res = await axios.post("https://ai-ops-561749935054.europe-west1.run.app/chat", { message })
      setResponse(res.data.reply)
    } catch (err) {
      console.error("Error:", err)
      setResponse("Something went wrong.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h2>💬 Ask a Question</h2>
      <textarea
        rows="4"
        cols="50"
        className="chat-textarea"
        placeholder="Curious about the contents of the uploaded document? Ask anything—whether it's a deep dive into specific details or a broad, general question. Your AI Document Assistant is here to help: from decoding complex information or summarizing content, to answering everyday queries."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <button onClick={sendMessage} className="chat-button" disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>
    </div>
  )
}

export default ChatWindow
