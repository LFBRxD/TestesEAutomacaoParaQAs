import http from 'k6/http';



export const options = {
    stages: [
        { duration: '10s', target: 100 }, // below normal load
        { duration: '2m', target: 100 },
        { duration: '10s', target: 200 }, // spike to 1400 users
        { duration: '2m', target: 200 }, // stay at 1400 for 3 minutes
        { duration: '10s', target: 500 }, // scale down. Recovery stage.
        { duration: '2m', target: 500 },
        { duration: '10s', target: 800 },
        { duration: '2m', target: 800 },
        { duration: '30s', target: 0 },
    ],

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