"use client";
import React, { createContext, useState, useEffect, ReactNode } from "react";
import {
  login,
  logout,
  isAuthenticated,
  getAccessToken,
  refreshToken,
} from "../utils/auth";
import { jwtDecode } from "jwt-decode";
import { DecodedToken } from "@/types";

export interface AuthContextProps {
  user: DecodedToken | null;
  handleLogin: (role: string, email: string, password: string) => Promise<void>;
  handleLogout: () => Promise<void>;
  handleRefresh: () => Promise<boolean>;
  isAuthenticated: () => boolean;
}

const AuthContext = createContext<AuthContextProps | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<DecodedToken | null>(null);

  useEffect(() => {
    const token = getAccessToken();
    if (token) {
      const decoded: DecodedToken = jwtDecode(token);
      decoded.role = localStorage.getItem("role") || "";
      setUser(decoded);
    }
  }, []);

  const handleLogin = async (role: string, email: string, password: string) => {
    const decoded = await login(role, email, password);
    decoded.role = role;
    setUser(decoded);
  };

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error(error);
    } finally {
      setUser(null);
    }
  };

  const handleRefresh = async () => {
    try {
      const refreshed = await refreshToken();
      return refreshed;
    } catch (error) {
      console.error(error);
      return false;
    }
  };
  return (
    <AuthContext.Provider
      value={{
        user,
        handleLogin,
        handleLogout,
        handleRefresh,
        isAuthenticated,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
