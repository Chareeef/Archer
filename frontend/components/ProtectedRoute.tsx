import { useContext, useEffect, ReactNode } from "react";
import { useRouter } from "next/router";
import AuthContext from "../context/AuthContext";

interface ProtectedRouteProps {
  children: ReactNode;
  allowedRoles?: string[];
}

const ProtectedRoute = ({ children, allowedRoles }: ProtectedRouteProps) => {
  const authContext = useContext(AuthContext);
  const router = useRouter();

  useEffect(() => {
    if (
      !authContext?.isAuthenticated() ||
      (allowedRoles &&
        typeof authContext.user?.role === "string" &&
        !allowedRoles.includes(authContext.user.role))
    ) {
      router.push("/login");
    }
  }, [authContext, authContext?.user, allowedRoles, router]);

  return authContext?.isAuthenticated() &&
    (!allowedRoles ||
      (typeof authContext.user?.role === "string" &&
        allowedRoles.includes(authContext.user.role))) ? (
    <>{children}</>
  ) : null;
};

export default ProtectedRoute;
