import React from 'react';
import { Route, Redirect } from 'react-router-dom';

const auth = true; 

const PublicRoute = ({ component: Component, restricted, ...rest }) => (
    <Route {...rest} render={props => (auth && restricted ? <Redirect to="/" /> : <Component {...props} />)} />
)

export default PublicRoute;