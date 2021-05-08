import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk, RootState } from "~/redux-recipies/store/app-store";

import { fetchUsers } from "./users-api";

export interface User {
  id: number;
  name: string;
  email: string;
}

export interface UsersState {
  users: User[];
  status: "idle" | "loading" | "failed";
}

const initialState: UsersState = {
  status: "idle",
  users: [],
};

export const usersSlice = createSlice({
  name: "users",
  initialState,
  reducers: {
    setUsers: (state, action: PayloadAction<User[]>) => {
      state.users = action.payload;
    },
  },
});

// async action to fetch asll users data.
export const fetchUsersData = (): AppThunk => async (dispatch) => {
  try {
    const response = await fetchUsers();
    const { data: users } = response;
    dispatch({ type: "users/setUsers", payload: users });
  } catch (error) {
    dispatch({ type: "users/setUsers", payload: [] });
  }
};

// selectors
export const selectUsers = (state: RootState) => state.user.users;

export default usersSlice.reducer;
