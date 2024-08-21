import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ApiButton from './components/APIButton'; // Adjust path as necessary
import Dashboard from './components/Dashboard'; // Adjust path as necessary

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<ApiButton />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </Router>
    );
    
};

export default App;
