import React from "react";
import { Route, Redirect } from "react-router-dom";

const PublicRoute = ({ component: Component, restricted, ...rest }) => {
  return (
    <Route {...rest} render={(props) => true && restricted ? <Redirect to="/" /> : <Component {...props} /> }/>
  )
};

export default PublicRoute;
