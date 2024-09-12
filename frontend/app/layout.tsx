import type { Metadata } from "next";
import { Open_Sans } from "next/font/google";
import { AuthProvider } from "@/context/AuthContext";
import { AlertProvider } from "@/context/AlertContext";
import { Analytics } from "@vercel/analytics/next";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import "./globals.css";

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
        <body className="relative flex flex-col items-center min-h-dvh">
          <AlertProvider>
            <Header />
            {children}
            <Footer />
          </AlertProvider>
          <Analytics />
        </body>
      </html>
    </AuthProvider>
  );
}
