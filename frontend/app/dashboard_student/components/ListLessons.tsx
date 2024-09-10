"use client";
import { useAlert } from "@/context/AlertContext";
import { Lesson } from "@/types";
import axiosClient from "@/utils/axiosClient";
import { useEffect, useState } from "react";

export default function ListLessons({ grade_level }: { grade_level: number }) {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const { showAlert } = useAlert();

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        const response = await axiosClient.get(
          `/curriculum/lessons/?grade_level=${grade_level}`,
        );
        const fetchedLessons = response.data.results;
        if (!Array.isArray(fetchedLessons)) {
          throw Error();
        }
        setLessons(fetchedLessons as Lesson[]);
      } catch (error) {
        showAlert("An error occured while fetching lessons.", "error");
      }
    };

    fetchLessons();
  }, []);

  return (
    <div className="p-4 md:col-span-3">
      {lessons && (
        <ul>
          {lessons.map((lesson) => (
            <li key={lesson.id}>
              {lesson.subject} | {lesson.grade_level} |{" "}
              {lesson.educator_full_name} | {lesson.title}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
