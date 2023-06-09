import axiosInstance from './index'

const axios = axiosInstance

export const addStar = (userId, bookId) => {
  return axios.post('http://127.0.0.1:8000/star/add_star', { user_id: userId, book_id: bookId })
}
export const deleteStar = (userId, bookId) => {
  return axios.post('http://127.0.0.1:8000/star/delete_star', { user_id: userId, book_id: bookId })
}
export const listStar = (userId) => {
  return axios.post('http://127.0.0.1:8000/star/list_star', { user_id: userId })
}
