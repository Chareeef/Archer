"use client";
import { FaPen } from "react-icons/fa6";
import { StudentDataFields } from "../types";

export default function StudentProfile({
  studentData,
  onOpen,
}: {
  studentData: StudentDataFields;
  onOpen: () => void;
}) {
  return (
    <div className="relative p-4 text-white border-r-2 md:col-span-1 bg-sky-700 border-sky-900">
      <button
        onClick={onOpen}
        className="absolute p-2 text-xs text-gray-700 bg-white border-2 border-gray-700 rounded-lg top-2 right-2"
      >
        {FaPen({})}
      </button>
      <h1 className="mb-4 text-xl font-bold text-center">Profile</h1>
      <ul className="flex flex-col items-center text-center space-y-4">
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">First Name:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.first_name}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Last Name:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.last_name}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Email:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.email}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Grade Level:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.grade_level}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Age:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.age}
          </span>
        </li>
        {studentData.parent_id && (
          <li className="flex flex-col items-center w-full">
            <span className="font-bold">Parent ID:</span>
            <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
              {studentData.parent_id}
            </span>
          </li>
        )}
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Sensory Preference:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.sensory_preference}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Communication Preference:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.communication_preference}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Attention Span:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.attention_span}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Reading/Writing Skills:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.reading_writing_skills}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Math Skills:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.math_skills}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Technology Comfort:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.technology_comfort}
          </span>
        </li>
        <li className="flex flex-col items-center w-full">
          <span className="font-bold">Interests:</span>
          <span className="w-full overflow-hidden text-center text-ellipsis whitespace-nowrap">
            {studentData.interests}
          </span>
        </li>
      </ul>
    </div>
  );
}
