import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  value: 0,
}

export const userLoginSlice = createSlice({
  name: 'userLogin',
  initialState,
  reducers: {
    USER_LOGIN_REQUEST: (state) => {
      state += 1
    },
    USER_LOGIN_SUCCESS: (state) => {
    },
    USER_LOGIN_FAIL: (state) => {
    },
    USER_LOGOUT: () => {
    }
  },
})

// Action creators are generated for each case reducer function
export const { USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGIN_FAIL, USER_LOGOUT } = userLoginSlice.actions

export default userLoginSlice.reducer