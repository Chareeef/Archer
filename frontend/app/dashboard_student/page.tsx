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
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);

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
  }, [isSettingsOpen]);

  return (
    <ProtectedRoute allowedRoles={["student"]}>
      <main className="flex w-full grow bg-sky-100">
        {studentData ? (
          <>
            <div className="relative h-full md:grid md:grid-cols-4 md:gap-0">
              <StudentProfile
                studentData={studentData}
                isProfileOpen={isProfileOpen}
                onProfileClose={() => setIsProfileOpen(false)}
                onSettingsOpen={() => setIsSettingsOpen(true)}
              />
              <ListLessons
                grade_level={studentData.grade_level}
                onProfileOpen={() => setIsProfileOpen(true)}
              />
            </div>

            {isSettingsOpen && (
              <UpdateProfileModal
                studentData={studentData}
                onClose={() => setIsSettingsOpen(false)}
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
