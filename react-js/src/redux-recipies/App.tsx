import React from "react";
import { Users } from "./users/Users";

export function App() {
  console.log("app rendered");

  return (
    <div className="m-2">
      <Users />
    </div>
  );
}
