
function get_request(endpoint){
    const url = 'http://192.168.4.187:5000/' + endpoint;
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json', // Specify the content type
        }
    };

    // Make the fetch request
    return fetch(url, options)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

export { get_request }