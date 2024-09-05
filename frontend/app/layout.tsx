import type { Metadata } from "next";
import "./globals.css";

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
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
