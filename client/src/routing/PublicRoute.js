import React, { useContext } from "react";
import { Route, Redirect } from "react-router-dom";
import { AuthContext } from '../context/AuthContext';

const PublicRoute = ({ component: Component, restricted, ...rest }) => {
  const { isAuthenticated } = useContext(AuthContext); 

  return (
    <Route {...rest} render={(props) => isAuthenticated && restricted ? <Redirect to="/" /> : <Component {...props} /> }/>
  )
};

export default PublicRoute;
