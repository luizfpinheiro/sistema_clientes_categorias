import axios from 'axios';

const api = axios.create({
    baseURL: 'http://172.21.0.3:8000',
});

export default api;
