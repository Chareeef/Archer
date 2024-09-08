"use client";
import { useContext, useEffect, ReactNode } from "react";
import { useRouter } from "next/navigation";
import AuthContext from "@/context/AuthContext";
import { useAlert } from "@/context/AlertContext";

interface ProtectedRouteProps {
  children: ReactNode;
  allowedRoles?: string[];
}

const ProtectedRoute = ({ children, allowedRoles }: ProtectedRouteProps) => {
  const authContext = useContext(AuthContext);
  const router = useRouter();
  const { showAlert } = useAlert();

  useEffect(() => {
    if (
      !authContext?.isAuthenticated() ||
      (allowedRoles &&
        typeof authContext.user?.role === "string" &&
        !allowedRoles.includes(authContext.user.role))
    ) {
      showAlert("You are not allowed to access this page.", "error");
      router.push("/signin");
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
