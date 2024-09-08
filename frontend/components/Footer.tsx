"use client";
import AuthContext from "@/context/AuthContext";
import Link from "next/link";
import { useContext } from "react";
import { FaGithub, FaLinkedin } from "react-icons/fa";

export default function Footer() {
  const authContext = useContext(AuthContext);

  return (
    <footer className="flex flex-col items-center justify-around w-full p-4 text-white border-t-2 gap-4 bg-sky-600 border-sky-800">
      <div className="flex flex-col flex-wrap w-full px-4 md:flex-row md:justify-between gap-y-4">
        {/* Team */}
        <div className="flex flex-col justify-around gap-y-4">
          <h3 className="ml-2 text-lg italic font-bold">Team:</h3>
          <div className="flex w-full gap-x-4">
            <h4 className="w-2/3 mr-2 font-semibold">Youssef Charif Hamidi:</h4>
            <Link
              className="hover:text-sky-800"
              href="https://github.com/Chareeef"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaGithub size={20} />
            </Link>
            <Link
              className="hover:text-sky-800"
              href="https://linkedin.com/in/youssef-charif-hamidi"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaLinkedin size={20} />
            </Link>
            <Link
              href="https://x.com/YoussefCharifH2"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-center hover:text-sky-800"
              style={{ width: "20px", height: "20px" }}
            >
              <span style={{ fontSize: "20px", fontWeight: "bold" }}>𝕏</span>
            </Link>
          </div>
          <div className="flex gap-x-4">
            <h4 className="w-2/3 mr-2 font-semibold">Qudsiya Badri:</h4>
            <Link
              className="hover:text-sky-800"
              href="https://linkedin.com/in/qudsiya-badri"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaLinkedin size={20} />
            </Link>
            <Link
              href="https://x.com/QudsiyaBadri"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-center hover:text-sky-800"
              style={{ width: "20px", height: "20px" }}
            >
              <span style={{ fontSize: "20px", fontWeight: "bold" }}>𝕏</span>
            </Link>
          </div>
        </div>

        {/* Important Links */}
        <div className="flex flex-col gap-y-2 md:w-[40%]">
          <h3 className="ml-2 text-lg italic font-bold">Important Links:</h3>
          <Link
            href="/"
            className="text-base hover:text-sky-200 hover:translate-x-4 transition-transform ease-out duration-300"
          >
            Home
          </Link>
          <Link
            href="/about"
            className="text-base hover:text-sky-200 hover:translate-x-4 transition-transform ease-out duration-300"
          >
            About
          </Link>
          {authContext?.user ? (
            <Link
              href={`/dashboard_${authContext.user.role}`}
              className="text-base hover:text-sky-200 hover:translate-x-4 transition-transform ease-out duration-300"
            >
              Dashboard
            </Link>
          ) : (
            <>
              <Link
                href="/signin"
                className="text-base hover:text-sky-200 hover:translate-x-4 transition-transform ease-out duration-300"
              >
                Sign In
              </Link>
              <Link
                href="/signup"
                className="text-base hover:text-sky-200 hover:translate-x-4 transition-transform ease-out duration-300"
              >
                Sign Up
              </Link>
            </>
          )}
        </div>
      </div>

      <p className="pt-2 mt-4 text-sm text-center border-t border-white">
        © 2024 ARCHER
      </p>
    </footer>
  );
}
