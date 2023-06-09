import axiosInstance from './index'

const axios = axiosInstance

export const addComment = (userId, bookId, rate, content) => {
  return axios.post('http://127.0.0.1:8000/comment/add_comment', { user_id: userId, book_id: bookId, rate: rate, content: content })
}
export const searchComment = (bookId) => {
  return axios.post('http://127.0.0.1:8000/comment/search_comment', { book_id: bookId })
}
