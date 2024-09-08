"use client";
import { useContext, useEffect, ReactNode } from "react";
import { useRouter } from "next/navigation";
import AuthContext, { AuthContextProps } from "@/context/AuthContext";
import { useAlert } from "@/context/AlertContext";

interface ProtectedRouteProps {
  children: ReactNode;
  allowedRoles?: string[];
}

const ProtectedRoute = ({ children, allowedRoles }: ProtectedRouteProps) => {
  const authContext = useContext(AuthContext) as AuthContextProps;
  const router = useRouter();
  const { showAlert } = useAlert();

  useEffect(() => {
    const checkUser = async () => {
      if (!authContext.isAuthenticated()) {
        // Attempt to refresh the token
        const refreshed = await authContext.handleRefresh();
        if (!refreshed) {
          showAlert("You are not allowed to access this page.", "error");
          router.push("/signin");
          return;
        }
      }

      if (
        allowedRoles &&
        typeof authContext.user?.role === "string" &&
        !allowedRoles.includes(authContext.user.role)
      ) {
        showAlert("You are not allowed to access this page.", "error");
        router.push("/signin");
      }
    };

    checkUser();
  }, [authContext, authContext?.user, allowedRoles, router]);

  return <>{children}</>;
};

export default ProtectedRoute;
