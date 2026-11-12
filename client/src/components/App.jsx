import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import './App.css';

function App() {
  const [apiStatus, setApiStatus] = useState('checking');
  const [workspaces, setWorkspaces] = useState([]);
  const [panes, setPanes] = useState([]);

  // API health check
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch('/api/v1/health');
        if (response.ok) {
          const data = await response.json();
          setApiStatus('healthy');
          setTimeout(loadData, 100);
        } else {
          setApiStatus('error');
        }
      } catch (error) {
        setApiStatus('error');
      }
    };
    
    checkHealth();
  }, []);

  const loadData = async () => {
    try {
      const [wsResponse, panesResponse] = await Promise.all([
        fetch('/api/v1/workspaces'),
        fetch('/api/v1/panes')
      ]);
      
      if (wsResponse.ok) {
        const wsData = await wsResponse.json();
        setWorkspaces(wsData.workspaces);
      }
      
      if (panesResponse.ok) {
        const panesData = await panesResponse.json();
        setPanes(panesData.panes);
      }
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <h1>Tensor Foundry-145</h1>
          <div className="status-bar">
            <span className={`status ${apiStatus}`}>API Status: {apiStatus}</span>
            <span className="version">v0.1.0</span>
          </div>
          
          <nav className="main-nav">
            <Link to="/workspaces" className="nav-link">Workspaces</Link>
            <Link to="/panes" className="nav-link">Panes</Link>
            <Link to="/sessions" className="nav-link">Sessions</Link>
          </nav>
          
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Workspaces</h3>
              <p className="stat-number">{workspaces.length}</p>
            </div>
            <div className="stat-card">
              <h3>Panes</h3>
              <p className="stat-number">{panes.length}</p>
            </div>
            <div className="stat-card">
              <h3>Agents</h3>
              <p className="stat-number">0</p>
            </div>
          </div>
          
          <div className="welcome-message">
            <h2>Welcome to Tensor Foundry-145</h2>
            <p>A terminal window manager that knows what your agents are doing.</p>
            <p>This initial skeleton provides the foundation for:</p>
            <ul>
              <li>Tiling panes and workspaces</li>
              <li>Sessions that survive restarts</li>
              <li>One Inbox for every coding agent</li>
              <li>Agent-aware window management</li>
            </ul>
            <p>Core workspace and pane management to be implemented in Phase 2.</p>
          </div>
        </header>
        
        <Routes>
          <Route path="/workspaces" element={<div>Workspaces Page</div>} />
          <Route path="/panes" element={<div>Panes Page</div>} />
          <Route path="/sessions" element={<div>Sessions Page</div>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
