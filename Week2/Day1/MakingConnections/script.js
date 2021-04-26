function editProfile() {
    var name = prompt("Please enter your name.", "Jane Doe")
    document.querySelector('#username').innerHTML = name;
}

function addConnection(user) {
    temp = document.querySelector(user);
    temp.remove();
    reduceRequests();
    addToConnection();
}

function removeConnection(user) {
    temp = document.querySelector(user);
    temp.remove();
    reduceRequests();
}

requestNum = parseInt(document.querySelector('#conReqNum').innerHTML)

function reduceRequests() {
    requestNum--;
    document.querySelector('#conReqNum').innerHTML = requestNum.toString(); 
}

connectionsNumber = parseInt(document.querySelector('#connectionNumber').innerHTML)

function addToConnection() {
    connectionsNumber++
    document.querySelector('#connectionNumber').innerHTML = connectionsNumber.toString();
}