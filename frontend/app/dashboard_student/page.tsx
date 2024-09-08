"use client";
import { useContext } from "react";
import ProtectedRoute from "@/components/ProtectedRoute";
import AuthContext, { AuthContextProps } from "@/context/AuthContext";

export default function StudentDashboard() {
  const { user } = useContext(AuthContext) as AuthContextProps;
  return (
    <ProtectedRoute allowedRoles={["student"]}>
      {JSON.stringify(user, null, 2)}
    </ProtectedRoute>
  );
}
