import { React, useContext } from 'react';
import { Route, Redirect } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import Navbar from '../components/core/Navbar';

const PrivateRoute = ({ component: Component, ...rest }) => {
    const { isAuthenticated } = useContext(AuthContext); 
    
    return (
        <Route {...rest} render={props => (isAuthenticated ? <><Navbar/><Component {...props} /></> : <Redirect to="/login" />)} />
    )
}

export default PrivateRoute; 