import { check } from 'k6';
import http from 'k6/http';


export const options = {
    vus: 100,
    duration: '60s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],

    },
};

export default function () {

    const resp = http.get('http://localhost:8080/users');
    //console.log(`Response time was ${resp.timings.duration} ms`);
    //console.log(`Response code was ${resp.status}`);
    //console.log(`Response body was ${resp.body}`);
    //
    check(resp, {
        'status is 200': (r) => r.status === 200,
        'response body': (r) => r.body.length > 0,
    });
}