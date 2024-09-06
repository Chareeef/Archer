import type { Metadata } from "next";
import "./globals.css";
import { AuthProvider } from "@/context/AuthContext";
import { AlertProvider } from "@/context/AlertContext";

export const metadata: Metadata = {
  title: "Archer",
  description: "Educational platform for children with autism.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <AuthProvider>
      <html lang="en">
        <body className="relative flex flex-col items-center justify-around">
          <header className="h-10 w-full flex items-center bg-black">
            header
          </header>
          <AlertProvider>{children}</AlertProvider>
          <footer className="h-10 w-full flex items-center bg-black">
            footer
          </footer>
        </body>
      </html>
    </AuthProvider>
  );
}
