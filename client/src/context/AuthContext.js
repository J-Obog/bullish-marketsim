import React, { useState, useEffect, createContext } from 'react';

export const AuthContext = createContext(null); 

const Auth = ({children}) => {
    const [token, setToken] = useState(null);  
    const [refresh, setRefreshToken] = useState(null);
    const [isAuthenticated, setAuthenticated] = useState(false);

    return (
        <AuthContext.Provider value={{ token, isAuthenticated }}>
            {children}
        </AuthContext.Provider>
    )
}; 

export default Auth;