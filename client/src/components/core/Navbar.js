import React from "react";
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
            <div className="bg-white py-5 px-4 flex flex-row items-center justify-between">
                <div className="flex flex-row">
                    <Link to="/" className="text-gray-800 mr-4 hover:text-green-300">Trading</Link>
                    <Link to="/orders" className="text-gray-800 mr-4 hover:text-green-300">Orders</Link>
                    <Link to="/portfolio" className="text-gray-800 mr-4 hover:text-green-300">Portfolio</Link>
                </div>
                <div className="flex flex-row">
                    <Link to="#" className="text-gray-800 mr-4 hover:text-green-300">Account</Link>
                </div>
            </div>
    );
}


export default Navbar;