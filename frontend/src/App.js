import React from "react";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import IpTagList from './components/IpTagList';

function App() {
  return (
      <Router>
        <div>
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="/">IP Tag Manager</a>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <a className="nav-link" href="/list">List</a>

                </li>
              </ul>
            </div>
          </nav>
          <div className="container mt-4">
            <Switch>
              <Route path="/" exact component="{IpTagList}" />
            </Switch>
          </div>
        </div>
      </Router>
  );
}