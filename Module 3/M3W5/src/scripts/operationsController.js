import useFetch from "./utils/fetch.js"

const URL = "http://localhost:3000/operations";

async function getOperations() {
    return await useFetch(URL, "GET")
}

async function getOperationsOfUserId(userId) {
    return await useFetch(`${URL}/?userId=${userId}`, "GET");
}

async function postOperation(body) {
    return await useFetch(URL, "POST", body);
}

async function patchOperation (id, body) {
    return await useFetch(`${URL}/${id}`, "PATCH", body);
}

async function deleteOperation (id) {
    return await useFetch(`${URL}/${id}`, "DELETE");
}

export default { getOperations, getOperationsOfUserId, postOperation, patchOperation, deleteOperation}