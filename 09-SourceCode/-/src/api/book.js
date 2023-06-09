import axiosInstance from './index'

const axios = axiosInstance

export const modifyBook = (bookId, bookName, label1, label2, introduce, authorName) => {
  return axios.post('http://127.0.0.1:8000/book/modifyBook', { book_id: bookId, book_name: bookName, book_main_type: label1, book_secondary_type: label2, book_introduction: introduce, book_author_name: authorName })
}
export const addBook = (bookName, label1, label2, introduce, authorName, rate, popularity, bookURL) => {
  return axios.post('http://127.0.0.1:8000/book/addBook', { book_name: bookName, book_main_type: label1, book_secondary_type: label2, book_introduction: introduce, book_author_name: authorName, book_score: rate, book_popularity: popularity, book_url: bookURL })
}
export const getBookById = (bookId) => {
  return axios.post('http://127.0.0.1:8000/book/getBookById', { book_id: bookId })
}
export const getAuthorBooks = (name) => {
  return axios.post('http://127.0.0.1:8000/book/getBookByAuthor', { book_author_name: name })
}
export const getBookId = (bookName) => {
  return axios.post('http://127.0.0.1:8000/book/getBookId', { book_name: bookName })
}
export const addPopularity = (bookId) => {
  return axios.post('http://127.0.0.1:8000/book/BookPopularityAdd', { book_id: bookId })
}
export const searchBookByKey = (key) => {
  return axios.post('http://127.0.0.1:8000/book/searchBookByKey', { key: key })
}
export const getBookByMainType = (main) => {
  return axios.post('http://127.0.0.1:8000/book/getBookByMainType', { book_main_type: main })
}
export const getBookByTwoType = (main, secondary) => {
  return axios.post('http://127.0.0.1:8000/book/getBookByTwoType', { book_main_type: main, book_secondary_type: secondary })
}
export const modifyRate = (bookId, rate) => {
  return axios.post('http://127.0.0.1:8000/book/modifyScore', { book_id: bookId, book_score: rate })
}
