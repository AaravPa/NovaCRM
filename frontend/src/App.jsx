import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ContactsPage from './pages/ContactsPage'
import LoginPage from './pages/LoginPage'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  if (!isAuthenticated) {
    return <LoginPage onLogin={() => setIsAuthenticated(true)} />
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ContactsPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
