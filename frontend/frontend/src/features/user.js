import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

const initialState = {
    isAuthenticated: false,
    user: null,
    loading: false,
    registered: false,
}

export const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    resetRegistered: state => {
      state.registered = false;
    }
  },
})

// Action creators are generated for each case reducer function
export const { resetRegiserted } = userSlice.actions

export default userSlice.reducer