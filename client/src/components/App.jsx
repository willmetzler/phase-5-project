import { Outlet } from 'react-router-dom'
import React from "react";
import Navbar from "../Navbar";

function App() {
  return (
    <div>

      <div>
        <h1>Header?</h1>
      </div>

      <div>
        <Navbar/>
      </div>

      <div>
        <Outlet />
      </div>
    </div>
  )
}

export default App;
