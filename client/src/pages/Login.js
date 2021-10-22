import React, { useState } from 'react'; 
import { Link } from 'react-router-dom';
import axios from "axios"; 

const Login = () => {
    const [email, setEmail] = useState(""); 
    const [password, setPassword] = useState(""); 
    const [erros, setErrors] = useState(null);

    const changeEmail = (e) => {
        setEmail(e.target.value); 
    }

    const changePassword = (e) => {
        setPassword(e.target.value); 
    }

    const attemptLogin = () => {
        axios.post("http://localhost:4001/api/auth/login", { email: email, password: password})
        .then(({data}) => {

        })
        .catch(err => {
            console.error(err);
        })
    }

    return (
        <div className="flex items-center justify-center h-screen">
            <div className="bg-white w-1/4 px-16 py-8 rounded-md shadow-xl flex flex-col items-center justify-center">
                <div className="mb-16">
                    <h1>Bullish Market Sim</h1>
                    <h2>Some other text</h2>
                </div>
                <div className="mb-12">
                    <div className="mb-8">
                        <input onInput={changeEmail} size="30" placeHolder="Email" className="outline-none border-b-2 border-gray-200 focus:border-green-300"/>
                    </div>
                    <div>
                        <input onInput={changePassword} size="30" type="password" placeHolder="Password" 
                        className={`(1) ? "" : "outline-none border-b-2 border-gray-200 focus:border-green-300`}/>
                    </div>
                </div>
                <div className="text-sm mb-10">
                    <Link to="/signup">Don't have an account?</Link>
                </div>
                <div className="mb-6 w-full">
                    <button onClick={attemptLogin} className="bg-green-400 py-1 px-3 text-white text-xl rounded-2xl w-full">Login</button>
                </div>
            </div>
        </div>
    )
}

export default Login; 