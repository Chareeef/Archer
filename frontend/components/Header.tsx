"use client";
import { useContext } from "react";
import AuthContext, { AuthContextProps } from "@/context/AuthContext";
import Link from "next/link";
import { useAlert } from "@/context/AlertContext";
import Image from "next/image";

export default function Header() {
  const { user, handleLogout } = useContext(AuthContext) as AuthContextProps;
  const { showAlert } = useAlert();

  const handleClickSignOut = async () => {
    try {
      handleLogout();
      showAlert("Signed out successfully.", "info");
    } catch (error) {
      console.error(error);
      showAlert("Something went wrong.", "error");
    }
  };

  return (
    <header className="flex flex-col items-center justify-between w-full p-4 text-center text-white border-b-2 bg-gradient-to-t from-sky-200 to-white border-sky-800 md:flex-row">
      <Link href="/" className="flex items-center text-xl">
        <Image
          src="/icons/logo.png"
          alt="Archer logo"
          height={96}
          width={142}
          className="h-[3.3rem] w-[5rem] mr-3"
        />
        <div className="text-2xl font-extrabold text-blue-800">Archer</div>
      </Link>
      <div className="flex items-center justify-around text-lg gap-x-4">
        {user ? (
          <>
            <Link href={`/dashboard_${user.role}`} className="btn-header">
              Dashboard
            </Link>
            <button onClick={handleClickSignOut} className="btn-header">
              Sign Out
            </button>
          </>
        ) : (
          <>
            <Link href={`/signup`} className="btn-header">
              Sign Up
            </Link>
            <Link href={`/signin`} className="btn-header">
              Sign In
            </Link>
          </>
        )}
      </div>
    </header>
  );
}