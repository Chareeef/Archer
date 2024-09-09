import Image from "next/image";
import Link from "next/link";

export default function LandingPage() {
  return (
    <main className="flex flex-col items-center w-full min-h-svh bg-blue-50">
      {/* Hero Section */}
      <section className="w-full py-12 text-center bg-blue-50">
        <div className="flex flex-col items-center justify-around p-4 md:flex-row gap-8">
          <h1 className="text-4xl font-bold text-blue-800">
            The world{"'"}s first education app tailored for children with
            autism
          </h1>
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
      <section className="w-full py-12 bg-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold text-blue-800">Features</h2>
          <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-12">
            {/* Feature 1 */}
            <div className="flex flex-col items-center">
              <Image
                src="/science.png"
                alt="Multi-sensory Learning"
                width={617}
                height={789}
                className="w-48 h-52"
              />
              <h3 className="mt-4 text-xl font-bold text-blue-700">Science</h3>
              <p className="mt-2 text-gray-600">
                Learning science never been more fun.
              </p>
            </div>

            {/* Feature 2 */}
            <div className="flex flex-col items-center">
              <Image
                src="/english.png"
                alt="Reading & Writing"
                width={617}
                height={789}
                className="w-48 h-52"
              />
              <h3 className="mt-4 text-xl font-bold text-blue-700">
                Reading & Writing
              </h3>
              <p className="mt-2 text-gray-600">
                Interactive tools and activities to enhance literacy skills.
              </p>
            </div>

            {/* Feature 3 */}
            <div className="flex flex-col items-center">
              <Image
                src="/mathematics.png"
                alt="Mathematics"
                width={617}
                height={789}
                className="w-48 h-52"
              />
              <h3 className="mt-4 text-xl font-bold text-blue-700">
                Mathematics
              </h3>
              <p className="mt-2 text-gray-600">
                Simplified tutorials to help students grasp math concepts.
              </p>
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
