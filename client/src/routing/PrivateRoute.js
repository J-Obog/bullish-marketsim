import { React } from 'react';
import { Route, Redirect } from 'react-router-dom';
import Navbar from '../components/core/Navbar';

const PrivateRoute = ({ component: Component, ...rest }) => {
    return (
        <Route {...rest} render={props => (true  ? <><Navbar/><Component {...props} /></> : <Redirect to="/login" />)} />
    )
}

export default PrivateRoute; 