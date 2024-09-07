"use client";
import { useState } from "react";

export default function ToggleSignup({
  onToggle,
}: {
  onToggle: (type: string) => void;
}) {
  const [active, setActive] = useState("Student");

  const handleToggle = (type: string) => {
    setActive(type);
    onToggle(type);
  };

  return (
    <div className="flex justify-center px-8 py-4 mx-auto mb-4 bg-gray-100 border-2 border-blue-500 w-fit space-x-4 rounded-md">
      {["Student", "Parent", "Educator"].map((type) => (
        <button
          key={type}
          onClick={() => handleToggle(type)}
          className={`px-4 py-2 ${active === type ? "bg-blue-500 text-white" : "bg-white text-blue-500"} rounded-md`}
        >
          {type}
        </button>
      ))}
    </div>
  );
}
