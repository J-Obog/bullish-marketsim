import React from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';
import { PrivateRoute, PublicRoute } from "./router-hooks"; 
import { Dashboard, Login, Logout, Orders, Portfolio, Signup, Stock, NoMatch } from "./pages"; 

const App = () => {
    return (
        <Router>
            <Switch>  
                <PublicRoute path="/login" component={Login} exact restricted/>
                <PublicRoute path="/signup" component={Signup} exact restricted/>
                <PrivateRoute path="/" component={Dashboard} exact />
                <PrivateRoute path="/orders" component={Orders} exact />
                <PrivateRoute path="/portfolio" component={Portfolio} exact />
                <PrivateRoute path="/stock/:id" component={Stock} exact />
                <PrivateRoute path="*" component={NoMatch} exact />
            </Switch>
        </Router>
    );
}

export default App;