import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8080'
});

// Interceptor para agregar el token a las peticiones
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authApi = {
  login: (credentials) => api.post('/auth/login', credentials),
  register: (userData) => api.post('/auth/register', userData),
};

export const usersApi = {
  getAll: () => api.get('/users'),
  create: (userData) => api.post('/users', userData),
};

export const municipiosApi = {
  getAll: () => api.get('/municipios'),
  create: (municipioData) => api.post('/municipios', municipioData),
};

export const territoriosApi = {
  getAll: () => api.get('/territorios'),
  create: (territorioData) => api.post('/territorios', territorioData),
};