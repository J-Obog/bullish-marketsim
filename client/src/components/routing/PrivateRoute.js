import { React, useContext } from 'react';
import { Route, Redirect } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import Navbar from '../core/Navbar';

const PrivateRoute = ({ component: Component, ...rest }) => {
    const { authenticated } = useContext(AuthContext); 
    
    return (
        <Route {...rest} render={props => (authenticated ? <><Navbar/><Component {...props} /></> : <Redirect to="/login" />)} />
    )
}

export default PrivateRoute; 