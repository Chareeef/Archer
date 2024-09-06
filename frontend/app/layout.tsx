import type { Metadata } from "next";
import { Open_Sans } from "next/font/google";
import "./globals.css";
import { AuthProvider } from "@/context/AuthContext";
import { AlertProvider } from "@/context/AlertContext";
import Header from "@/components/Header";

export const metadata: Metadata = {
  title: "Archer",
  description: "Educational platform for children with autism.",
};

const OpenSans = Open_Sans({ weight: "400", subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <AuthProvider>
      <html lang="en" className={OpenSans.className}>
        <body className="relative flex flex-col items-center justify-around">
          <AlertProvider>
            <Header />
            {children}
          </AlertProvider>
          <footer className="flex items-center w-full h-10 bg-black">
            footer
          </footer>
        </body>
      </html>
    </AuthProvider>
  );
}