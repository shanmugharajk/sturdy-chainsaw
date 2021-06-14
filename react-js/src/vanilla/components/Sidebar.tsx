import React from "react";
import { Link } from "react-router-dom";

export const Sidebar: React.FunctionComponent<
  React.HTMLAttributes<HTMLDivElement>
> = ({ ...styleProps }) => {
  return (
    <div {...styleProps}>
      <ul className="space-x-4 space-y-5 text-sm text-gray-500">
        <li />
        <li>
          <Link className="hover:text-gray-900" to="/">
            Home
          </Link>
        </li>

        <li>
          <Link className="hover:text-gray-900" to="/key-index-issue">
            Key index issue
          </Link>
        </li>

        <li>
          <Link className="hover:text-gray-900" to="/will-not-match">
            Will Not Match
          </Link>
        </li>
      </ul>
    </div>
  );
};
