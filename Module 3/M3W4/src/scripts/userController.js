import useFetch from "./utils/fetch.js"

const URL_USER = "http://localhost:3000/users"

async function getUsers () {
    return await useFetch(URL_USER, "GET");
}

async function getUser(id) {
    return await useFetch(`${URL_USER}/?id=${id}`, "GET");
}

async function getUserByEmail(email) {
    return await useFetch(`${URL_USER}/?email=${email}`, "GET");
}

async function postUser (body) {
    return await useFetch(URL_USER, "POST", body);
}

async function patchUser (id, body) {
    return await useFetch(`${URL_USER}/${id}`, "PATCH", body);
}

async function deleteUser (id) {
    return await useFetch(`${URL_USER}/${id}`, "DELETE");
}

export default { getUsers, getUser, getUserByEmail, postUser, patchUser, deleteUser };