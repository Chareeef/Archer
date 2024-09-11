import Image from "next/image";
import Link from "next/link";

export default function LandingPage() {
  return (
    <main className="flex flex-col items-center w-full min-h-svh bg-blue-50">
      {/* Hero Section */}
      <section className="w-full py-12 text-center bg-blue-50">
        <div className="flex flex-col items-center justify-around p-4 md:flex-row gap-8">
          <div className="flex-col">
            <h1 className="mb-4 font-extrabold text-blue-800 text-7xl">
              ARCHER
            </h1>
            <h2 className="text-2xl font-bold text-blue-800">
              The world{"'"}s first education app tailored for children with
              autism.
            </h2>
          </div>
          <Image
            src="/target.png"
            alt="target"
            width={753}
            height={807}
            className="w-[15rem] h-[16rem]"
          />
          {/*
          <p className="mt-4 text-lg text-gray-600">
            Join our waitlist to get notified!
          </p>
          <div className="flex justify-center mt-6">
            <input
              type="email"
              placeholder="Enter your email address"
              className="px-4 py-2 border border-gray-300 rounded-l-md focus:outline-none"
            />
            <button className="px-6 py-2 text-white bg-blue-500 rounded-r-md hover:bg-blue-600">
              Join Waitlist
            </button>
          </div>*/}
        </div>
      </section>

      {/* Features Section */}
      <section className="w-full px-4 py-12 bg-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold text-blue-800">Features</h2>
          <div className="flex flex-col mt-8">
            {/* Reading & Writing */}
            <div className="flex flex-col w-full md:grid md:grid-cols-2 gap-16">
              <Image
                src="/reading_writing.png"
                alt="Reading & Writing"
                width={1024}
                height={1024}
                className="size-auto"
              />
              <div className="flex flex-col items-center justify-center">
                <h3 className="mt-4 text-xl font-bold text-blue-700">
                  Reading & Writing
                </h3>
                <p className="mt-2 text-gray-600">
                  Reading & Writing Interactive tools and activities designed to
                  enhance literacy skills and make learning fun.
                </p>
              </div>
            </div>

            {/* Mathematics */}
            <div className="flex flex-col-reverse w-full md:grid md:grid-cols-2 gap-16">
              <div className="flex flex-col items-center justify-center">
                <h3 className="mt-4 text-xl font-bold text-blue-700">
                  Mathematics
                </h3>
                <p className="mt-2 text-gray-600">
                  Simplified tutorials and exercises to help students grasp math
                  concepts with ease.
                </p>
              </div>
              <Image
                src="/mathematics.png"
                alt="Mathematics"
                width={1024}
                height={1024}
                className="size-auto"
              />
            </div>

            {/* Science */}
            <div className="flex flex-col w-full md:grid md:grid-cols-2 gap-16">
              <Image
                src="/science.png"
                alt="Science"
                width={1024}
                height={1024}
                className="size-auto"
              />
              <div className="flex flex-col items-center justify-center">
                <h3 className="mt-4 text-xl font-bold text-blue-700">
                  Science
                </h3>
                <p className="mt-2 text-gray-600">
                  Engaging experiments and lessons to foster curiosity and
                  understanding in science.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Help Us Improve Section */}
      <section className="flex flex-col items-center w-full px-4 py-12 text-center bg-blue-100">
        <h2 className="text-3xl font-bold text-blue-800">Help Us Improve!</h2>
        <p className="mt-4 text-gray-600">
          Your feedback will help shape ARCHER Education to meet students{"' "}
          unique needs.
        </p>
        <Link
          href="/signup"
          className="px-8 py-3 mt-6 text-white bg-blue-500 w-fit rounded-md hover:bg-blue-600"
        >
          Sign Up Now!
        </Link>
      </section>
    </main>
  );
}
