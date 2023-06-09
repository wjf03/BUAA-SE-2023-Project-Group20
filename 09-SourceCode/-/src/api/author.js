import axiosInstance from './index'

const axios = axiosInstance

export const getAuthor = (name) => {
  return axios.post('http://127.0.0.1:8000/author/search_author', { name: name })
}
export const modifyAuthor = (id, introduction) => {
  return axios.post('http://127.0.0.1:8000/author/edit_author', { id: id, introduction: introduction })
}
export const addAuthor = (name, introduction) => {
  return axios.post('http://127.0.0.1:8000/author/add_author', { name: name, introduction: introduction })
}
