import { React } from 'react';
import { Route, Redirect } from 'react-router-dom';
//import AuthContext from '../context/AuthContext';

const PrivateRoute = ({ component: Component, ...rest }) => {
    //const {} = localStorage.getItem('auth:rfsh')
    
    return (
        <Route {...rest} render={props => (true ? <Component {...props} /> : <Redirect to="/login" />)} />
    )
}
export default PrivateRoute; 