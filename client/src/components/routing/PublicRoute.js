import React, { useContext } from "react";
import { Route, Redirect } from "react-router-dom";
import { AuthContext } from '../../context/AuthContext';

const PublicRoute = ({ component: Component, restricted, ...rest }) => {
  const { authenticated } = useContext(AuthContext); 

  return (
    <Route {...rest} render={(props) => authenticated && restricted ? <Redirect to="/" /> : <Component {...props} /> }/>
  )
};

export default PublicRoute;
