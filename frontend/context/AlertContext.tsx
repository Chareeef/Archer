"use client";
import { createContext, useContext, useState, ReactNode } from "react";

interface AlertContextProps {
  showAlert: (message: string, type: "success" | "error" | "info") => void;
}

const AlertContext = createContext<AlertContextProps | undefined>(undefined);

export const AlertProvider = ({ children }: { children: ReactNode }) => {
  const [alert, setAlert] = useState<{ message: string; type: string } | null>(
    null,
  );
  const [isVisible, setIsVisible] = useState(false);

  const showAlert = (message: string, type: "success" | "error" | "info") => {
    setAlert({ message, type });
    setIsVisible(true); // Show the alert

    // Automatically hide the alert after 3 seconds
    setTimeout(() => {
      setIsVisible(false); // Start hiding the alert with transition
      setTimeout(() => {
        setAlert(null); // Remove the alert after the transition is done
      }, 500); // The duration of the fade-out transition
    }, 3000); // Alert stays visible for 3 seconds
  };

  return (
    <AlertContext.Provider value={{ showAlert }}>
      {alert && (
        <div
          className={`fixed top-[10svh] flex items-center justify-center px-2 py-1 rounded-lg text-center w-fit ${isVisible ? "opacity-100" : "opacity-0"} transition-all duration-500 ease-in-out ${getAlertClasses(alert.type)}`}
        >
          {alert.message}
        </div>
      )}
      {children}
    </AlertContext.Provider>
  );
};

const getAlertClasses = (type: string) => {
  switch (type) {
    case "success":
      return "bg-green-500 text-white";
    case "error":
      return "bg-red-500 text-white";
    case "info":
      return "bg-blue-500 text-white";
    default:
      return "";
  }
};

export const useAlert = () => {
  const context = useContext(AlertContext);
  if (!context) {
    throw new Error("useAlert must be used within an AlertProvider");
  }
  return context;
};
