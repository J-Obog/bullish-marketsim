import React, { useEffect, useState } from "react";

//routing
import { Switch, BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import PrivateRoute from "./routing/PrivateRoute";
import PublicRoute from "./routing/PublicRoute";

//pages
import { Dashboard, Login, Logout, Orders, Portfolio, Signup, Stock, NoMatch } from "./pages";

import Auth from './context/AuthContext'; 

const App = () => {
    return (
        <Router>
            <Auth>
                
            </Auth>
        </Router>
    );
}

export default App;