"use client";
import ProtectedRoute from "@/components/ProtectedRoute";
import { useAlert } from "@/context/AlertContext";
import { Lesson } from "@/types";
import axiosClient from "@/utils/axiosClient";
import Image from "next/image";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

export default function LessonPage() {
  const { id } = useParams();
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const { showAlert } = useAlert();

  useEffect(() => {
    const fetchLesson = async () => {
      try {
        const response = await axiosClient.get(
          `/curriculum/lessons/retrieve_lesson/${id}`,
        );
        const fetchedLesson = response.data;
        setLesson(fetchedLesson as Lesson);
      } catch (error) {
        if ((error as { status: number }).status !== 404) {
          showAlert("An error occured while fetching lesson.", "error");
        }
      }
    };

    fetchLesson();
  }, [id, showAlert]);

  return (
    <ProtectedRoute>
      <main className="flex flex-col items-center w-full p-4 grow gap-y-4">
        {lesson ? (
          <>
            <div className="flex flex-col items-center w-full overflow-hidden border-2 rounded-lg shadow-md md:grid md:grid-cols-2 divide-y-2 md:divide-y-0 md:divide-x-2 divide-sky-800 gap-0 bg-sky-300 border-sky-800">
              <Image
                src={`/${lesson.subject.toLowerCase().replace(" & ", "_")}.png`}
                alt={lesson.subject}
                width={1024}
                height={1024}
                className="w-full h-auto"
              />

              <div className="flex flex-col items-center justify-center w-full h-full p-4 text-center gap-y-4">
                <h1 className="text-4xl font-bold">{lesson.title}</h1>
                <h2 className="text-3xl font-semibold">
                  {lesson.subject} | Grade Level: {lesson.grade_level}
                </h2>
                <h2 className="text-2xl font-semibold">
                  By {lesson.educator_full_name}
                </h2>
                <h3 className="text-xl font-semibold text-gray-700">
                  Created At: {lesson.created_at}
                </h3>
              </div>
            </div>

            <div className="w-full p-4 bg-white border-2 rounded-lg shadow-2xl max-w-none prose border-sky-800">
              <ReactMarkdown>{lesson.text}</ReactMarkdown>
            </div>
          </>
        ) : (
          <div className="flex items-center justify-center text-gray-700 grow">
            Lesson Not Found
          </div>
        )}
      </main>
    </ProtectedRoute>
  );
}
