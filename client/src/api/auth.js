import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const useAuth = () => {
  const { token } = useContext(AuthContext);

  const validateToken = () => {
    return 0;
  };

  return {
    validateToken,
  };
};

export default useAuth;
