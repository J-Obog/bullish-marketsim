import React from 'react';
import { Route, Redirect } from 'react-router-dom';

const auth = true; 

const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => (auth ? <Component {...props} /> : <Redirect to="/login" />)} />
)
export default PrivateRoute;