"use client";
import axios from "axios";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAlert } from "@/context/AlertContext";

const API_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL;

export default function EducatorSignupForm() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    first_name: "",
    last_name: "",
    parentId: "",
    grade_level: 0,
    subject: "Reading & Writing",
  });
  const { showAlert } = useAlert();
  const router = useRouter();

  // Subjects
  const subjects = ["Reading & Writing", "Mathematics", "Science"];

  const handleSelect = (field: string, value: string) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post(`${API_URL}/users/signup/educator/`, formData);
      showAlert(
        `Welcome ${formData.first_name}! You can sign in now.`,
        "success",
      );
      router.push("/signin");
    } catch (error) {
      const dataError = error as {
        response?: { data?: Record<string, string[]> };
      };
      const data = dataError.response?.data;

      if (data) {
        let errorString = "";

        for (const key in data) {
          if (data.hasOwnProperty(key)) {
            errorString += `${key}: ${data[key][0]}\n`;
          }
        }

        showAlert(errorString, "error");
      } else {
        showAlert("Sorry, a server error occured.", "error");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <input
        type="email"
        value={formData.email}
        placeholder="Email"
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        className="w-full p-2 border rounded-md"
        required
      />
      <input
        type="password"
        value={formData.password}
        placeholder="Password"
        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
        className="w-full p-2 border rounded-md"
        required
      />
      <input
        type="text"
        value={formData.first_name}
        placeholder="First Name"
        onChange={(e) =>
          setFormData({ ...formData, first_name: e.target.value })
        }
        className="w-full p-2 border rounded-md"
        required
      />
      <input
        type="text"
        value={formData.last_name}
        placeholder="Last Name"
        onChange={(e) =>
          setFormData({ ...formData, last_name: e.target.value })
        }
        className="w-full p-2 border rounded-md"
        required
      />
      <input
        type="number"
        value={formData.grade_level || ""}
        placeholder="Grade Level"
        onChange={(e) =>
          setFormData({ ...formData, grade_level: parseInt(e.target.value) })
        }
        className="w-full p-2 border rounded-md"
        required
      />

      {/* Subject */}
      <div className="w-full space-y-2">
        <p>Subject</p>
        <div className="flex flex-wrap items-center justify-center gap-4">
          {subjects.map((subject) => (
            <button
              type="button"
              key={subject}
              onClick={() => handleSelect("subject", subject)}
              className={`px-4 py-2 rounded-md ${
                formData.subject === subject
                  ? "bg-blue-500 text-white"
                  : "bg-gray-200"
              }`}
            >
              {subject}
            </button>
          ))}
        </div>
      </div>

      <button
        type="submit"
        className="block px-4 py-2 mx-auto text-white btn rounded-md"
      >
        Sign Up as Educator
      </button>
    </form>
  );
}
