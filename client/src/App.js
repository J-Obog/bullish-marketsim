import React from "react";

//routing
import { Switch, BrowserRouter as Router } from "react-router-dom";
import PrivateRoute from "./routing/PrivateRoute";
import PublicRoute from "./routing/PublicRoute";

//pages
import { Dashboard, Login, Logout, Orders, Portfolio, Signup, Stock, NoMatch } from "./pages";

import Auth from './context/AuthContext'; 

const App = () => {
    return (
        <Router>
            <Auth>
                <Switch>
                    <PublicRoute path="/login" component={Login} exact restricted/>
                    <PublicRoute path="/signup" component={Signup} exact restricted/>
                    <PrivateRoute path="/" component={Dashboard} exact />
                    <PrivateRoute path="/orders" component={Orders} exact />
                    <PrivateRoute path="/portfolio" component={Portfolio} exact />
                    <PrivateRoute path="/stock/:id" component={Stock} exact />
                    <PrivateRoute path="*" component={NoMatch} exact />
                </Switch>
            </Auth>
        </Router>
    );
}

export default App;