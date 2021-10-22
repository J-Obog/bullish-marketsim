import React, { useState, useEffect, createContext } from 'react';
import axios from "axios"; 

export const AuthContext = createContext(null); 

const Auth = ({children}) => {
    const [access, setAccessToken] = useState(localStorage.getItem('auth-access'));  
    const [refresh, setRefreshToken] = useState(localStorage.getItem('auth-refresh'));
    const [authenticated, setAuthenticated] = useState(false);
    
    useEffect(() => {
        if(!access || !refresh)
            return;  
            
        axios.get("http://localhost:4001/api/auth/verify", { headers: { 'auth-access': access, 'auth-refresh': refresh }})
        .then(res => {
            setAuthenticated(true); 
        })
        .catch(err => { 
            console.error(err); 
        })

    },[access, refresh])

    const login = (accessToken, refreshToken) => {
        localStorage.setItem('auth-access', accessToken);
        localStorage.setItem('auth-refresh', refreshToken);
        setAccessToken(accessToken); 
        setRefreshToken(refreshToken);   
        setAuthenticated(true);
    }

    const logout = () => {
        localStorage.setItem('auth-access', null); 
        localStorage.setItem('auth-refresh', null); 
        setAccessToken(null); 
        setRefreshToken(null);   
        setAuthenticated(false); 
    }

    return (
        <AuthContext.Provider value={{ access, refresh, authenticated, logout, login }}>
            {children}
        </AuthContext.Provider>
    )
}; 

export default Auth;