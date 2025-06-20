import { useState } from 'react'
import axios from 'axios'
import '../App.css'

function FileUploader() {
  const [file, setFile] = useState(null)
  const [status, setStatus] = useState("")

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
    setStatus("")
  }

  const uploadFile = async () => {
    if (!file) {
      setStatus("Please select a file.")
      return
    }

    const formData = new FormData()
    formData.append("file", file)

    try {
      const res = await axios.post("https://ai-ops-561749935054.europe-west1.run.app/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      })
      setStatus(res.data.message)
    } catch (err) {
      console.error(err)
      setStatus("Upload failed.")
    }
  }

  return (
    <div>
      <h2>📄 Upload PDF</h2>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <br /><br />
      <button onClick={uploadFile}>Upload</button>
      <p>{status}</p>
    </div>
  )
}

export default FileUploader
