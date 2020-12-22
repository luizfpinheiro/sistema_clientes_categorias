const axios = require('axios');

function get(url) {
    return axios.get(url);
}

function post(url, params) {
    return axios.post(url, params);
}

function put(url, params) {
    return axios.put(url, params);
}

function remove(url, params) {
    return axios.delete(url, params);
}


export default { get, post, put, remove }

