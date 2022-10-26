import React, { useState } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import './App.css'
import Dashboard from '../Dashboard/Dashboard'
import Login from '../Login/Login'
import Preferences from '../Preferences/Preferences'
import Grid from '../Grid/Grid'
import Grouping from '../Grouping/Grouping'

// function setToken(userToken) {
//   sessionStorage.setItem('token', JSON.stringify(userToken));
// }

// function getToken() {
//   const tokenString = sessionStorage.getItem('token');
//   const userToken = JSON.parse(tokenString);
//   return userToken?.token
// }

function App() {
  const [token, setToken] = useState()
  // const token = getToken();

  /* if (!token) {
    return <Login setToken={setToken} />
  } */

  return (
    <div>
      <h1>
        <Grouping />
      </h1>
      <BrowserRouter>
        <Routes>
          <Route path="/grid" element={<Grid />}></Route>
          <Route path="/dashboard" element={<Dashboard />}></Route>
          <Route path="/preferences" element={<Preferences />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
