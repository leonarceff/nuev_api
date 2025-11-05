import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Interceptor para agregar el token a las peticiones
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Si recibimos un 401, el token puede haber expirado
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    console.error('API Error:', error.response);
    throw error;
  }
);

// API endpoints
const endpoints = {
  auth: {
    login: (credentials) => api.post('/auth/login', credentials),
    register: (userData) => api.post('/auth/register', userData),
  },
  users: {
    getAll: () => api.get('/users'),
    create: (userData) => api.post('/users', userData),
  },
  municipios: {
    getAll: () => api.get('/municipios'),
    create: (data) => api.post('/municipios', data),
  },
  territorios: {
    getAll: () => api.get('/territorios'),
    create: (data) => api.post('/territorios', data),
  }
};

export { api, endpoints };

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