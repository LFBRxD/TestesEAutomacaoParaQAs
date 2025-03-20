import http from 'k6/http';



export const options = {
    vus: 5000,
    duration: '1s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],

    },
};

export default function () {
    const randomEmail = `user_${Math.floor(Math.random() * 10000)}@email.com`;
    const randomName = `TesteName${Math.floor(Math.random() * 1000)} LastName${Math.floor(Math.random() * 1000)} `;
    const randomDocument = `${Math.floor(10000000000 + Math.random() * 90000000000)}`;

    const url = 'http://localhost:8080/user';
    
    const payload = JSON.stringify({
        email: randomEmail,
        name: randomName,
        document: randomDocument,
    });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    http.post(url, payload, params);
}