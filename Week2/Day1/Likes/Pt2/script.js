var users = {
    neilM: 0,
}

function addLike(username) {
    if (users[username] == null) {
        users[username] = 0;
    }
    console.log(username);
    users[username] += 1;
    console.log(users[username])
    document.getElementById(username).innerText = `${users[username]} likes(s)`;
}

