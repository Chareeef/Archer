"use client";
import { useEffect, useState } from "react";
import ProtectedRoute from "@/components/ProtectedRoute";
import axiosClient from "@/utils/axiosClient";
import { StudentDataFields } from "./types";
import StudentProfile from "./components/StudentProfile";
import UpdateProfileModal from "./components/UpdateStudentProfile";
import ListLessons from "./components/ListLessons";

export default function StudentDashboard() {
  const [studentData, setStudentData] = useState<StudentDataFields | undefined>(
    undefined,
  );
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axiosClient.get("/users/student");
        setStudentData(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [isModalOpen]);

  return (
    <ProtectedRoute allowedRoles={["student"]}>
      <main className="flex w-full grow bg-sky-100">
        {studentData ? (
          <>
            <div className="md:grid md:grid-cols-4 md:gap-0">
              <StudentProfile
                studentData={studentData}
                onOpen={() => setIsModalOpen(true)}
              />
              <ListLessons grade_level={studentData.grade_level} />
            </div>

            {isModalOpen && (
              <UpdateProfileModal
                studentData={studentData}
                onClose={() => setIsModalOpen(false)}
              />
            )}
          </>
        ) : (
          <div className="flex items-center justify-center w-full text-lg text-center text-gray-400">
            No data. Try to renew your session.
          </div>
        )}
      </main>
    </ProtectedRoute>
  );
}
