"use client";
import { useState } from "react";
import { useAlert } from "@/context/AlertContext";
import axiosClient from "@/utils/axiosClient";
import { StudentDataFields } from "../types";
import { FaX } from "react-icons/fa6";

const API_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL;

export default function UpdateProfileModal({
  studentData,
  onClose,
}: {
  studentData: StudentDataFields;
  onClose: () => void;
}) {
  const [formData, setFormData] = useState(studentData);
  const { showAlert } = useAlert();

  const sensoryPreferences = [
    "Low contrast",
    "High contrast",
    "No sound effects",
    "Background music",
  ];
  const communicationPreferences = ["Verbal", "Non-verbal"];
  const attentionSpans = ["Short", "Moderate", "Long"];
  const readingWritingSkills = [
    "Emerging",
    "Basic",
    "Intermediate",
    "Advanced",
  ];
  const mathSkills = ["Emerging", "Basic", "Intermediate", "Advanced"];
  const technologyComfortLevels = [
    "Very comfortable",
    "Comfortable",
    "Needs assistance",
    "Uncomfortable",
  ];
  const childInterests = [
    "Animals",
    "Space & Astronomy",
    "Vehicles",
    "Nature & Environment",
    "Superheroes",
    "Sports",
    "Fantasy & Fairy tales",
  ];

  const handleSelect = (field: string, value: string) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axiosClient.put(`${API_URL}/users/student/`, formData);
      showAlert(`Your profile has been updated!`, "success");
      onClose();
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
    <div className="z-40 fixed inset-0 flex items-center justify-center p-8 bg-gray-800 h-dvh bg-opacity-50">
      <div className="relative w-full h-full text-sm bg-white rounded-lg shadow-lg md:text-lg">
        <div className="w-full h-full p-4 overflow-y-auto">
          <h2 className="mb-4 text-2xl font-bold">Update Profile</h2>
          <button
            onClick={onClose}
            className="absolute z-20 p-2 text-white bg-red-500 w-fit -top-4 -right-4 hover:bg-red-700 hover:scale-110 rounded-md"
          >
            <FaX />
          </button>
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Basic Fields */}
            <p>Email</p>
            <input
              type="email"
              value={formData.email}
              placeholder="Email"
              onChange={(e) =>
                setFormData({ ...formData, email: e.target.value })
              }
              className="w-full p-2 border rounded-md"
              required
            />

            <p>First Name</p>
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

            <p>Last Name</p>
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

            <p>Parent ID (optional)</p>
            <input
              type="text"
              value={formData.parent_id || ""}
              placeholder="Parent ID (optional)"
              onChange={(e) =>
                setFormData({ ...formData, parent_id: e.target.value })
              }
              className="w-full p-2 border rounded-md"
            />

            <p>Grade Level</p>
            <input
              type="number"
              value={formData.grade_level || ""}
              placeholder="Grade Level"
              onChange={(e) =>
                setFormData({
                  ...formData,
                  grade_level: parseInt(e.target.value),
                })
              }
              className="w-full p-2 border rounded-md"
              required
            />

            <p>Age</p>
            <input
              type="number"
              value={formData.age || ""}
              placeholder="Age"
              onChange={(e) =>
                setFormData({ ...formData, age: parseInt(e.target.value) })
              }
              className="w-full p-2 border rounded-md"
              required
            />

            {/* Preferences */}
            {/* Sensory Preference */}
            <div className="w-full space-y-2">
              <p>Sensory Preference</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {sensoryPreferences.map((preference) => (
                  <button
                    type="button"
                    key={preference}
                    onClick={() =>
                      handleSelect("sensory_preference", preference)
                    }
                    className={`px-4 py-2 rounded-md ${
                      formData.sensory_preference === preference
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {preference}
                  </button>
                ))}
              </div>
            </div>

            {/* Communication Preference */}
            <div className="w-full space-y-2">
              <p>Communication Preference</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {communicationPreferences.map((preference) => (
                  <button
                    type="button"
                    key={preference}
                    onClick={() =>
                      handleSelect("communication_preference", preference)
                    }
                    className={`px-4 py-2 rounded-md ${
                      formData.communication_preference === preference
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {preference}
                  </button>
                ))}
              </div>
            </div>

            {/* Attention Span */}
            <div className="w-full space-y-2">
              <p>Attention Span</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {attentionSpans.map((span) => (
                  <button
                    type="button"
                    key={span}
                    onClick={() => handleSelect("attention_span", span)}
                    className={`px-4 py-2 rounded-md ${
                      formData.attention_span === span
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {span}
                  </button>
                ))}
              </div>
            </div>

            {/* Reading & Writing Skills */}
            <div className="w-full space-y-2">
              <p>Reading & Writing Skills</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {readingWritingSkills.map((skill) => (
                  <button
                    type="button"
                    key={skill}
                    onClick={() =>
                      handleSelect("reading_writing_skills", skill)
                    }
                    className={`px-4 py-2 rounded-md ${
                      formData.reading_writing_skills === skill
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {skill}
                  </button>
                ))}
              </div>
            </div>

            {/* Math Skills */}
            <div className="w-full space-y-2">
              <p>Math Skills</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {mathSkills.map((skill) => (
                  <button
                    type="button"
                    key={skill}
                    onClick={() => handleSelect("math_skills", skill)}
                    className={`px-4 py-2 rounded-md ${
                      formData.math_skills === skill
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {skill}
                  </button>
                ))}
              </div>
            </div>

            {/* Technology Comfort Level */}
            <div className="w-full space-y-2">
              <p>Technology Comfort Level</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {technologyComfortLevels.map((level) => (
                  <button
                    type="button"
                    key={level}
                    onClick={() => handleSelect("technology_comfort", level)}
                    className={`px-4 py-2 rounded-md ${
                      formData.technology_comfort === level
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {level}
                  </button>
                ))}
              </div>
            </div>

            {/* Interests */}
            <div className="w-full space-y-2">
              <p>Interests</p>
              <div className="flex flex-wrap items-center justify-center gap-4">
                {childInterests.map((interest) => (
                  <button
                    type="button"
                    key={interest}
                    onClick={() => handleSelect("interests", interest)}
                    className={`px-4 py-2 rounded-md ${
                      formData.interests === interest
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200"
                    }`}
                  >
                    {interest}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex items-center justify-center w-full gap-x-6">
              <button
                type="submit"
                className="px-4 py-2 text-white btn rounded-md"
              >
                Update Profile
              </button>
              <button
                onClick={onClose}
                className="px-4 py-2 text-white bg-red-500 border-2 border-gray-400 transition-transform ease-in-out duration-300 hover:bg-red-700 hover:scale-110 rounded-md"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>{" "}
      </div>
    </div>
  );
}
