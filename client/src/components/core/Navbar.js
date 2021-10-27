import React from "react";
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
            <div className="bg-white py-5 px-4 flex flex-row items-center justify-between">
                <div className="flex flex-row">
                    <div className="mr-8 flex flex-row border border-gray-200 rounded-md px-2 py-0.5 hover:shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="#CBD5E1">
                            <path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd" />
                        </svg>
                        <input placeHolder="Lookup a Stock" className="bg-transparent outline-none"/>
                    </div>
                    <div>
                        <Link to="/" className="text-gray-800 mr-4 hover:text-green-300">Trading</Link>
                        <Link to="/orders" className="text-gray-800 mr-4 hover:text-green-300">Orders</Link>
                        <Link to="/portfolio" className="text-gray-800 mr-4 hover:text-green-300">Portfolio</Link>
                    </div>
                </div>
                <div className="flex flex-row">
                    <Link to="#" className="text-gray-800 mr-4 hover:text-green-300">Account</Link>
                </div>
            </div>
    );
}


export default Navbar;