// const url = 'http://192.168.4.187:5000/'
const url = 'https://ec2-3-133-151-61.us-east-2.compute.amazonaws.com/'
function get_request(endpoint){
    const my_url = url + endpoint;
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
    .then(data =>{
        return data
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
function get_user(){
    const endpoint = `get_user?access_token=${encodeURIComponent(sessionStorage.getItem("token"))}&refresh_token=${encodeURIComponent(sessionStorage.getItem("refresh"))}` 
    return get_request(endpoint).then(data => {
        return data
    })
}
function retrieve_email(){
    const endpoint = `get_email?access_token=${encodeURIComponent(sessionStorage.getItem("token"))}&refresh_token=${encodeURIComponent(sessionStorage.getItem("refresh"))}`
    return get_request(endpoint).then(data =>{
        return data["message"]
    })
}
function get_posts(){
    const endpoint = `get_posts?access_token=${encodeURIComponent(sessionStorage.getItem("token"))}&refresh_token=${encodeURIComponent(sessionStorage.getItem("refresh"))}`
    return get_request(endpoint).then(data => {
        return data
    })
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

function new_user(access_token, refresh_token){
    const my_url = url + 'new_user'
    const data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
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
function like_post(s_key){
    const my_url = url + 'post_interaction'
    const data = {
        "access_token": sessionStorage.getItem("token"),
        "refresh_token": sessionStorage.getItem("refresh"),
        "type": "like",
        "s_key": s_key
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
function dislike_post(s_key){
    const my_url = url + 'post_interaction'
    const data = {
        "access_token": sessionStorage.getItem("token"),
        "refresh_token": sessionStorage.getItem("refresh"),
        "type": "dislike",
        "s_key": s_key
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
export { new_post, del_post, retrieve_email, new_user, like_post, dislike_post, get_user, get_posts}