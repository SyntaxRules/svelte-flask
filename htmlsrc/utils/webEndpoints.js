export function getRandomNumber() {
    return get('/rand');
}

export function get(url) {
    return fetch(url).then(r => r.json());
}