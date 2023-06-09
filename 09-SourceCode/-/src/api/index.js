import { createApp } from 'vue'
import { reactive } from 'vue'
import Axios from 'axios'

const axiosInstance = Axios.create({
  withCredentials: true
})

// 通过拦截器处理 CSRF 问题，这里的正则和匹配下标可能需要根据实际情况进行调整
axiosInstance.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest'
  const regex = /.*csrftoken=([^;.]*).*$/
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
  return config
})

axiosInstance.interceptors.response.use(
  response => {
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

const app = createApp({})
app.config.globalProperties.axios = axiosInstance
app.config.globalProperties.$reactive = reactive

export { app }
export default axiosInstance