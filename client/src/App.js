import React, { useEffect, useState } from "react";
//routing
import { Switch, BrowserRouter as Router } from "react-router-dom";
import PrivateRoute from "./routing/PrivateRoute";
import PublicRoute from "./routing/PublicRoute";

//pages
import { Dashboard, Login, Logout, Orders, Portfolio, Signup, Stock, NoMatch } from "./pages";

import Navbar from './components/core/Navbar';
import AuthContext from "./context/AuthContext"; 

const App = () => {
    const [user, setUser] = useState({token: null, refresh: null, isAuthenticated: false}); 
    const BASE_URI = "http://localhost:4001/";

    useEffect(() => {
        //auth stuff
    }, [])

    return (
        <Router>
            <AuthContext.Provider value={{ user, setUser }}
            >
              { user.isAuthenticated && <Navbar/> }
              <Switch>  
                  <PublicRoute path="/login" component={Login} exact restricted/>
                  <PublicRoute path="/signup" component={Signup} exact restricted/>
                  <PrivateRoute path="/" component={Dashboard} exact/>
                  <PrivateRoute path="/orders" component={Orders} exact/>
                  <PrivateRoute path="/portfolio" component={Portfolio} exact/>
                  <PrivateRoute path="/stock/:id" component={Stock} exact/>
                  <PrivateRoute path="*" component={NoMatch} exact/>
              </Switch>
            </AuthContext.Provider>
        </Router>
    );
}

export default App;