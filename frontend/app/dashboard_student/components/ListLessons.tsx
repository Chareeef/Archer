"use client";
import { useAlert } from "@/context/AlertContext";
import { Lesson } from "@/types";
import axiosClient from "@/utils/axiosClient";
import Image from "next/image";
import { useEffect, useState } from "react";

function Lessons({
  grade_level,
  subject_key,
  subject_value,
}: {
  grade_level: number;
  subject_key: string;
  subject_value: string;
}) {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const { showAlert } = useAlert();

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        const response = await axiosClient.get(
          `/curriculum/lessons/?grade_level=${grade_level}&subject__iexact=${subject_value.replace("&", "%26")}`,
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
    <div>
      <h2 className="pl-4 my-2 text-lg font-bold border-l-4 border-sky-500">
        {subject_value} :
      </h2>
      {lessons.length > 0 ? (
        <ul className="flex p-4 overflow-x-auto gap-x-4">
          {lessons.map((lesson) => (
            <li
              className="flex flex-col w-[30%] shadow-md shrink-0 bg-amber-200 rounded-md"
              key={lesson.id}
            >
              <Image
                src={`/${subject_key}.png`}
                alt={subject_value}
                width={1024}
                height={1024}
                className="size-auto"
              />

              <div className="flex flex-col p-2 grow">
                <div className="flex items-center justify-center grow">
                  <h1 className="text-lg font-bold text-center">
                    {lesson.title}
                  </h1>
                </div>
                <h2 className="text-lg">By {lesson.educator_full_name}</h2>
                <p className="text-sm text-gray-600">{lesson.created_at}</p>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p className="flex items-center justify-center w-full h-20 text-gray-500">
          {subject_value} lessons will be available soon.
        </p>
      )}
    </div>
  );
}

export default function ListLessons({ grade_level }: { grade_level: number }) {
  return (
    <div className="p-4 md:col-span-3">
      <Lessons
        grade_level={grade_level}
        subject_key="reading_writing"
        subject_value="Reading & Writing"
      />

      <Lessons
        grade_level={grade_level}
        subject_key="mathematics"
        subject_value="Mathematics"
      />

      <Lessons
        grade_level={grade_level}
        subject_key="science"
        subject_value="Science"
      />
    </div>
  );
}
