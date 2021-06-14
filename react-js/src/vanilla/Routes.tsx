import React from "react";
import { Switch, Route } from "react-router-dom";

import { KeyIndexIssue } from "./key-index-issue";

export const Routes: React.FunctionComponent<
  React.HTMLAttributes<HTMLDivElement>
> = ({ ...styleProps }) => {
  return (
    <div {...styleProps}>
      <Switch>
        <Route exact path="/">
          Welcome to react essentials!
        </Route>

        <Route path="/key-index-issue">
          <KeyIndexIssue />
        </Route>

        <Route path="*">
          <div className="p-5 mr-3 border border-gray-200 rounded-md">
            Oops, not found!
          </div>
        </Route>
      </Switch>
    </div>
  );
};
