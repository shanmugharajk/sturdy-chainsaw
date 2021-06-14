import "~/index.css";

import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";

import { Header } from "~/vanilla/components/Header";
import { Sidebar } from "~/vanilla/components/Sidebar";

import { Routes } from "./Routes";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Header />
      <main className="flex space-x-3 space-y-4">
        <Sidebar className="w-60 min-h-screen border-r border-gray-100" />
        <Routes className="flex-1" />
      </main>
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);
