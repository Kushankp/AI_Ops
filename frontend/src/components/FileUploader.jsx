import { useState } from 'react'
import axios from 'axios'

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
      const res = await axios.post("https://c92a5e29-ef5c-4e14-b72f-7fc2b227cc1b-00-3mc63l854b256.pike.replit.dev/upload", formData, {
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
