import axios from 'axios';

const api = axios.create({
    baseURL: 'http://172.19.0.4:8000',
});

export default api;
