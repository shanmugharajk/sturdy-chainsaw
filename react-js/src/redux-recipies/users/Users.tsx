import React from "react";
import { useAppSelector, useAppDispatch } from "~/redux-recipies/store/hooks";

import { fetchUsersData, selectUsers } from "./users-slice";

export const Users: React.FunctionComponent = () => {
  const users = useAppSelector(selectUsers);
  const dispatch = useAppDispatch();

  React.useEffect(() => {
    dispatch(fetchUsersData());
  }, [dispatch]);

  return (
    <div>
      <h2 className="text-2xl">Users List</h2>

      <ul className="w-96 text-gray-900 text-sm my-4 border-l border-r border-t border-gray-200">
        {users.map((user) => (
          <li key={user.id} className="p-2 border-b border-gray-200">
            {user.id} - {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
};
