import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [notes, setNotes] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/notes')
      .then(res => setNotes(res.data))
      .catch(err => console.error("Erreur API:", err))
  }, [])

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Mes Notes 📝</h1>
      {notes.map(note => (
        <div key={note.id} style={{ border: '1px solid #ccc', margin: '10px 0', padding: '10px' }}>
          <h3>{note.title}</h3>
          <p>{note.content}</p>
        </div>
      ))}
    </div>
  )
}

export default App