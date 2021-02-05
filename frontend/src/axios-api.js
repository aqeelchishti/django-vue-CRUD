import axios from "axios";

const allAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    timeout: 1000,
    headers: {
        "Content-type": "application/json"
    }
});

export { allAPI };

/*export default axios.create({
    baseUrl: "http://127.0.0.1:8000/api",
    timeout: 1000,
    headers: {
        "Content-type": "application/json"
    }
});*/