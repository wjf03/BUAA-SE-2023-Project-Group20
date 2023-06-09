import axiosInstance from './index'

const axios = axiosInstance

export const getChapters = (bookId) => {
  return axios.post('http://127.0.0.1:8000/chapter/get_chapter', { book_id: bookId })
}
export const addChapters = (bookId, chapterNo, chapterName, chapterHref) => {
  return axios.post('http://127.0.0.1:8000/chapter/add_chapter', { book_id: bookId, chapter_no: chapterNo, chapter_name: chapterName, chapter_href: chapterHref })
}
