import axios from "axios";
import { jwtDecode } from "jwt-decode";
import { DecodedToken } from "@/types";

const API_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL;

interface LoginResponse {
  access: string;
  refresh: string;
}

export const login = async (
  role: string,
  email: string,
  password: string,
): Promise<DecodedToken> => {
  const response = await axios.post<LoginResponse>(
    `${API_URL}/users/signin/${role}/`,
    { email, password },
  );
  localStorage.setItem("access_token", response.data.access);
  localStorage.setItem("refresh_token", response.data.refresh);
  localStorage.setItem("role", role);
  const decoded: DecodedToken = jwtDecode(response.data.access);
  return decoded;
};

export const refreshToken = async (): Promise<boolean> => {
  const refresh_token = localStorage.getItem("refresh_token");
  try {
    const response = await axios.post<LoginResponse>(
      `${API_URL}/users/token/refresh/`,
      { refresh: refresh_token },
    );
    localStorage.setItem("access_token", response.data.access);
    return true;
  } catch (error) {
    return false;
  }
};

export const getAccessToken = (): string | null => {
  // Check if we're in a browser environment (client-side)
  if (typeof window !== "undefined" && typeof localStorage !== "undefined") {
    const token = localStorage.getItem("access_token");
    return token;
  }
  return null; // Return null if we're on the server side
};

export const isAuthenticated = (): boolean => {
  const token = getAccessToken();
  if (!token) return false;
  const decoded: DecodedToken = jwtDecode(token);
  return decoded.exp > Date.now() / 1000;
};

export const logout = async (): Promise<void> => {
  const refresh_token = localStorage.getItem("refresh_token");
  await axios.post(`${API_URL}/users/signout/`, { refresh: refresh_token });
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
};
