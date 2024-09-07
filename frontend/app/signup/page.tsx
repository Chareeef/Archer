"use client";
import { useState } from "react";
import ToggleSignup from "./components/ToggleSignup";
import StudentSignupForm from "./components/StudentSignupForm";
import ParentSignupForm from "./components/ParentSignupForm";
import EducatorSignupForm from "./components/EducatorSignupForm";
import Image from "next/image";

export default function Signup() {
  const [formType, setFormType] = useState("Student");

  const renderForm = () => {
    switch (formType) {
      case "Student":
        return <StudentSignupForm />;
      case "Parent":
        return <ParentSignupForm />;
      case "Educator":
        return <EducatorSignupForm />;
      default:
        return null;
    }
  };

  return (
    <main className="w-full p-4 md:px-16 bg-sky-100">
      <div className="p-4 bg-white shadow-lg">
        <Image
          src="/icons/logo.png"
          alt="Archer logo"
          height={96}
          width={142}
          className="h-[6.6rem] w-[10rem] mx-auto"
        />
        <h1 className="mb-4 text-2xl font-bold text-center">Sign Up</h1>
        <ToggleSignup onToggle={setFormType} />
        <div className="text-center">{renderForm()}</div>
      </div>
    </main>
  );
}
