import React from "react";
import { useAppSelector, useAppDispatch } from "~/redux-recipies/store/hooks";

import { fetchUsersData, selectUserState } from "./users-slice";

export const Users: React.FunctionComponent = () => {
  const userState = useAppSelector(selectUserState);
  const dispatch = useAppDispatch();

  React.useEffect(() => {
    dispatch(fetchUsersData());
  }, [dispatch]);

  return (
    <div>
      <h2 className="text-2xl">Users List</h2>

      {userState.status === "loading" && <div className="my-3">loading...</div>}

      {userState.status === "failed" && (
        <div className="w-96 my-4 p-3 border border-red-300 bg-red-50 text-red-400 rounded-md">
          You got an error
        </div>
      )}

      {userState.status === "idle" && (
        <ul className="w-96 text-gray-900 text-sm my-4 border-l border-r border-t border-gray-200">
          {userState.users.map((user) => (
            <li key={user.id} className="p-2 border-b border-gray-200">
              {user.id} - {user.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
