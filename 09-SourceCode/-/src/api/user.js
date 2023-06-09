import axiosInstance from './index'

const axios = axiosInstance

export const registercommon = (username, passwords) => 
{return axios.post(`http://127.0.0.1:8000/user/register`, 
{'username': username, 'password': passwords, 'ifManager': 0})}

export const registerManager = (username, passwords) => 
{return axios.post(`http://127.0.0.1:8000/user/register`, 
{'username': username, 'password': passwords, 'ifManager': 1})}

export const logout = () => 
{return axios.post(`http://127.0.0.1:8000/user/logout`)}

export const login = (username, password) => 
{return axios.post(`http://127.0.0.1:8000/user/login`, 
{'username': username, 'password': password})}

export const getUser = (userid) => 
{return axios.post(`http://127.0.0.1:8000/user/getUser`, {'user_id': userid})}


export const modifyUser = (userid, usernick, feormale) => 
{return axios.post(`http://127.0.0.1:8000/user/modifyUser`, 
{'user_id': userid, 'username': usernick, 'sex': feormale})}


