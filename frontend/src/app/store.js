import { configureStore } from '@reduxjs/toolkit'
import userLoginReducer from '../features/user/userLoginSlice'

export const store = configureStore({
  reducer: {
      user: userLoginReducer,
  },
})