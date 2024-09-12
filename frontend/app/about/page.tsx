"use client";
import Image from "next/image";
import AOS from "aos";
import { useEffect } from "react";

export default function About() {
  useEffect(() => {
    AOS.init({
      offset: 10,
      once: true,
      easing: "ease-out",
      duration: 300,
    });
  }, []);

  return (
    <main className="w-full grow divide-y-2 divide-sky-600">
      {/* Mission Section */}
      <section className="flex flex-col items-center justify-center px-8 py-12 text-center bg-sky-300 gap-y-4">
        <Image
          src="/icons/logo.png"
          alt="Archer logo"
          height={96}
          width={142}
          className="h-[6.6rem] w-[10rem] mx-auto"
          data-aos="fade-up"
        />

        <h1
          className="text-2xl italic font-bold underline md:text-3xl"
          data-aos="fade-up"
        >
          Our Mission:
        </h1>

        <h2 className="max-w-4xl text-lg font-bold" data-aos="fade-up">
          Our mission is to ensure that every student, regardless of their
          cognitive abilities, has access to quality education—anywhere,
          anytime.
        </h2>
      </section>

      {/* Story Section */}
      <section className="px-8 py-12 bg-white">
        <div className="max-w-4xl mx-auto text-lg text-center space-y-4">
          <h2
            className="mb-6 text-2xl font-bold md:text-3xl"
            data-aos="fade-up"
          >
            The Story Behind ARCHER
          </h2>
          <p data-aos="fade-up">
            Archer was designed with the belief that every child, regardless of
            their cognitive abilities, has the right to learn in a way that
            resonates with them. We wanted to build an app that was more than
            just a tool; we wanted it to be a companion that understands,
            adapts, and grows with each student.
          </p>
          <p data-aos="fade-up">
            This app is more than just a project—it’s our mission to redefine
            what education can be for students who learn differently. It’s about
            giving every child the opportunity to unlock their potential, to
            learn in a way that makes sense to them, and to build the essential
            life skills that will carry them forward.
          </p>
        </div>
      </section>

      {/* Impact Section */}
      <section className="px-4 py-12 bg-sky-500">
        <div className="max-w-5xl mx-auto text-center">
          <h2
            className="mb-6 text-2xl font-bold md:text-3xl"
            data-aos="fade-up"
          >
            Impact
          </h2>
          <div className="overflow-hidden grid grid-cols-1 md:grid-cols-3 gap-6">
            <div
              className="flex items-center justify-center p-6 bg-white rounded-lg shadow-lg"
              data-aos="fade-right"
            >
              <h3 className="text-lg font-semibold">
                Transforming Access to Education
              </h3>
            </div>
            <div
              className="flex items-center justify-center p-6 bg-white rounded-lg shadow-lg"
              data-aos="fade-right"
            >
              <h3 className="text-lg font-semibold">
                Empowering Every Learner
              </h3>
            </div>
            <div
              className="flex items-center justify-center p-6 bg-white rounded-lg shadow-lg"
              data-aos="fade-right"
            >
              <h3 className="text-lg font-semibold">
                Building a More Inclusive Future
              </h3>
            </div>
          </div>
        </div>
      </section>

      {/* Support Section */}
      <section className="px-6 py-12 text-center bg-blue-50">
        <h2 className="mb-6 text-2xl font-bold md:text-3xl" data-aos="fade-up">
          Support the Future of Accessible Education
        </h2>
        <p className="max-w-4xl mx-auto mb-6 text-lg" data-aos="fade-up">
          Every child deserves the opportunity to learn and thrive. Your
          donation helps us ensure that students with disabilities have access
          to the education they deserve. Stand with us in making education a
          right, not a privilege.
        </p>
        {/*  <button className="px-6 py-3 font-semibold text-white bg-blue-500 rounded-lg" data-aos="fade-up">
          Donate
        </button>
        */}
      </section>
    </main>
  );
}
