import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { AuthProvider } from "./context/Auth";
import "./styles/tokens.css"; import "./styles/app.css";
document.documentElement.dataset.theme = localStorage.getItem("theme") || "light";
createRoot(document.getElementById("root")).render(<BrowserRouter><AuthProvider><App /></AuthProvider></BrowserRouter>);
