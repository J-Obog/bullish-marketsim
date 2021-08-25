import React, { useState } from "react";

//routing
import { Switch, BrowserRouter as Router } from "react-router-dom";
import PrivateRoute from "./routing/PrivateRoute";
import PublicRoute from "./routing/PublicRoute";

//pages
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Logout from "./pages/Logout"; 
import Orders from "./pages/Orders";
import Portfolio from "./pages/Portfolio";
import Signup from "./pages/Signup";
import Stock from "./pages/Stock"; 
import NoMatch from "./pages/NoMatch"; 

import Navbar from './components/core/Navbar';
import AuthContext from "./context/AuthContext"; 

const App = () => {
    const [token, setToken] = useState("");

    return (
        <Router>
            <AuthContext.Provider value={{ token, setToken }}>
              <Navbar/>
              <Switch>  
                  <PublicRoute path="/login" component={Login} exact restricted/>
                  <PublicRoute path="/signup" component={Signup} exact restricted/>
                  <PrivateRoute path="/" component={Dashboard} exact />
                  <PrivateRoute path="/orders" component={Orders} exact />
                  <PrivateRoute path="/portfolio" component={Portfolio} exact />
                  <PrivateRoute path="/stock/:id" component={Stock} exact />
                  <PrivateRoute path="*" component={NoMatch} exact />
              </Switch>
            </AuthContext.Provider>
        </Router>
    );
}

export default App;