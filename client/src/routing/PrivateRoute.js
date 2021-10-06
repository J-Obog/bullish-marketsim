import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import useAuth from "../api/auth"; 


const PrivateRoute = ({ component: Component, ...rest }) => {
    const { validateToken } = useAuth();
    console.log(validateToken()); 
    return (
        <Route {...rest} render={props => (true ? <Component {...props} /> : <Redirect to="/login" />)} />
    )
}
export default PrivateRoute; 