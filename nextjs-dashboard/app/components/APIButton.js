'use client';
import axios from 'axios';
import { useState } from 'react';
import qs from 'qs';
import '../style/global.css'; // Import the CSS file
import { useNavigate } from '../pages/api/auth/useNavigates';

const ApiButton = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const [token, setToken] = useState('');
    const [isLogin, setIsLogin] = useState(true);
    const { navigateToDashboard } = useNavigate();

    // Function to handle user registration
    const handleRegistration = async () => {
        try {
            const response = await axios.post('/api/register', {
                username, email, password
            });
            console.log('Registration Response:', response.data);
            setMessage(`Registration successful: ${response.data.message || 'User registered successfully!'}`);
            navigateToDashboard();
           
        } catch (error) {
            console.error('Registration Error:', error);
            setMessage(`Error: ${error.response?.data?.error || error.message}`);
        }
    };

    // Function to handle user login
    const handleLogin = async () => {
        try {
            const credentials = { username, password };
            console.log('Login Credentials:', credentials);
            const response = await axios.post('http://192.168.1.5450/auth/login', qs.stringify(credentials), {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            });
            console.log('Login Response:', response.data);
            if (response.data?.access_token) {
                setToken(response.data.access_token);
                setMessage(`Login Successful! Token: ${response.data.access_token}`);
                navigateToDashboard();
            } else {
                setMessage('Login Successful but no access token received');
            }
        } catch (error) {
            console.error('Login Error:', error);
            setMessage(`Error: ${error.response?.data?.detail || error.message}`);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (isLogin) {
            handleLogin();
        } else {
            handleRegistration();
        }
    };

    return (
        <div className="container">
            <h2>{isLogin ? 'Login' : 'Sign Up'}</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </label>
                {!isLogin && (
                    <label>
                        Email:
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </label>
                )}
                <label>
                    Password:
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>
                <button type="submit">{isLogin ? 'Login' : 'Sign Up'}</button>
            </form>
            <button className="switch-button" onClick={() => setIsLogin(!isLogin)}>
                {isLogin ? 'Switch to Sign Up' : 'Switch to Login'}
            </button>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default ApiButton;
