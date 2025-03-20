import http from 'k6/http';
import { check } from 'k6';


export const options = {
    vus: 5000,
    duration: '1s',
};

export default function () {
    const resp = http.get('http://localhost:8080/users');
}