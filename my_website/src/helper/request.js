const url = 'http://192.168.4.187:5000/'
function get_request(endpoint, access_token, refresh_token){
    const my_url = url + endpoint + `?access_token=${encodeURIComponent(access_token)}&refresh_token=${encodeURIComponent(refresh_token)}`;
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json', 
        }
    };

    return fetch(my_url, options)
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
function new_post(title, msg, access_token, refresh_token){
    const my_url = url + 'new_post';
    const data = {
    'title': title,
    'msg': msg,
    'access_token': access_token,
    'refresh_token': refresh_token
    };
    
    return fetch(my_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
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
function del_post(p_key, s_key, access_token, refresh_token){
    const my_url = url + 'delete_post';
    const data = {
        'p_key': p_key,
        's_key': s_key,
        'access_token': access_token,
        'refresh_token': refresh_token
    };
    
    return fetch(my_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
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
function retrieve_email(access_token, refresh_token){
    const my_url = url + `get_email?access_token=${encodeURIComponent(access_token)}&refresh_token=${encodeURIComponent(refresh_token)}`;
    return fetch(my_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if(!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        
        return response.json()
    })
    .then(data => {
        console.log(data)
        return data["message"]
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error)
    })
}
function new_user(access_token, refresh_token){
    console.log("got here")
    const my_url = url + 'new_user'
    const data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
    };
    sessionStorage.setItem("data", data)
    console.log(data)
    return fetch(my_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
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
export { get_request, new_post, del_post, retrieve_email, new_user }