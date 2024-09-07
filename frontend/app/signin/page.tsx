"use client";
import React, { useState, useContext } from "react";
import AuthContext from "@/context/AuthContext";
import { useRouter } from "next/navigation";
import { useAlert } from "@/context/AlertContext";
import Image from "next/image";

const SignIn = () => {
  const { handleLogin } = useContext(AuthContext)!;
  const { showAlert } = useAlert();
  const router = useRouter();
  const [role, setRole] = useState("student");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await handleLogin(role, email, password);
      showAlert("Signed in successfully!", "success");
      router.push("/");
    } catch (err) {
      const error = err as { status: number };
      const status_code = error.status as number;
      if (status_code === 401) {
        showAlert("Sorry, your credentials are invalid", "error");
      } else {
        showAlert("Sorry, a server error occurred.", "error");
      }
    }
  };

  return (
    <div className="flex flex-col items-center justify-center w-full min-h-screen bg-sky-100">
      <div className="w-full max-w-md px-12 py-4 bg-white rounded-lg shadow-md">
        <Image
          src="/icons/logo.png"
          alt="Archer logo"
          height={96}
          width={142}
          className="h-[6.6rem] w-[10rem] mx-auto"
        />
        <h1 className="mb-4 text-2xl font-bold text-center">Sign In</h1>

        {/* Toggle Bar */}
        <div className="flex justify-around mt-4">
          {["student", "parent", "educator"].map((r) => (
            <button
              key={r}
              onClick={() => setRole(r)}
              className={`px-4 py-2 rounded-full ${
                role === r
                  ? "bg-blue-500 text-white"
                  : "bg-gray-200 text-gray-700"
              }`}
            >
              {r.charAt(0).toUpperCase() + r.slice(1)}
            </button>
          ))}
        </div>

        <form onSubmit={onSubmit} className="mt-6">
          <div>
            <label
              htmlFor="email"
              className="block text-sm font-medium text-gray-700"
            >
              Email
            </label>
            <input
              id="email"
              type="email"
              className="block w-full p-2 mt-1 border rounded-md bg-gray-50"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="mt-4">
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-700"
            >
              Password
            </label>
            <input
              id="password"
              type="password"
              className="block w-full p-2 mt-1 border rounded-md bg-gray-50"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button
            type="submit"
            className="w-full py-2 mt-6 text-white btn rounded-md"
          >
            Sign In as {role.charAt(0).toUpperCase() + role.slice(1)}
          </button>
        </form>
      </div>
    </div>
  );
};

export default SignIn;
