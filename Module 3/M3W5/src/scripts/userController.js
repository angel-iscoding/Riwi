import useFetch from "./utils/fetch.js"

const URL = "http://localhost:3000/users"

async function getUsers () {
    return await useFetch(URL, "GET");
}

async function getUser(id) {
    return await useFetch(`${URL}/?id=${id}`, "GET");
}

async function getUserByEmail(email) {
    return await useFetch(`${URL}/?email=${email}`, "GET");
}

async function thisEmailExist(email) {
    const user = await useFetch(`${URL}/?email=${email}`, "GET");
    return user ? true : false;     
}

async function thisIdExist(id) {
    const user = await useFetch(`${URL}/?id=${id}`, "GET");
    return user ? true : false;     
}

async function postUser (body) {
    return await useFetch(URL, "POST", body);
}

async function patchUser (id, body) {
    return await useFetch(`${URL}/${id}`, "PATCH", body);
}

async function deleteUser (id) {
    return await useFetch(`${URL}/${id}`, "DELETE");
}

export default { getUsers, getUser, getUserByEmail, thisEmailExist, thisIdExist, postUser, patchUser, deleteUser };