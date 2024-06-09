import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import IpTagList from './components/IpTagList';
import IpTagCreate from './components/IpTagCreate';
import IpTagUpdate from './components/IpTagUpdate';

function App() {
  return (
      <Router>
        <div>
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="/">IP Tag Manager</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <a className="nav-link" href="/list">List</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/create">Create</a>
                </li>
              </ul>
            </div>
          </nav>
          <div className="container mt-4">
            <Routes>
              <Route path="/" element={<IpTagList/>}/>
              <Route path="/list" element={<IpTagList/>}/>
              <Route path="/create" element={<IpTagCreate/>}/>
              <Route path="/update/:pk" element={<IpTagUpdate />} />
            </Routes>
          </div>
        </div>
      </Router>
  );
}

export default App