function getCurrentUser(){
    const dataJson = localStorage.getItem("dataIdentity");
    const identity = JSON.parse(dataJson);
    return identity.identification;
}
export default getCurrentUser