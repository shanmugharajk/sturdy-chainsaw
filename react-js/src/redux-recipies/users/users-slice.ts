import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk, RootState } from "~/redux-recipies/store/app-store";

import { fetchUsers } from "./users-api";

export interface User {
  id: number;
  name: string;
  email: string;
}

export type Status = "idle" | "loading" | "failed";
export interface UsersState {
  users: User[];
  status: Status;
}

const initialState: UsersState = {
  status: "idle",
  users: [],
};

export const usersSlice = createSlice({
  name: "users",
  initialState,
  reducers: {
    setStatus: (state, action: PayloadAction<Status>) => {
      state.status = action.payload;
    },
    setError: (state) => {
      state.status = "failed";
      state.users = [];
    },
    setUsers: (state, action: PayloadAction<User[]>) => {
      state.users = action.payload;
      state.status = "idle";
    },
  },
});

// async action to fetch asll users data.
export const fetchUsersData = (): AppThunk => async (dispatch) => {
  try {
    dispatch({ type: "users/setStatus", payload: "loading" });

    const response = await fetchUsers();
    const { data: users } = response;

    dispatch({ type: "users/setUsers", payload: users });
  } catch (error) {
    dispatch({ type: "users/setError" });
  }
};

// selectors
export const selectUserState = (state: RootState) => state.user;

export default usersSlice.reducer;
