import useFetch from "./utils/fetch.js"

const URL_EVENT = "http://localhost:3000/events"

async function getEvents () {
    return await useFetch(URL_EVENT, "GET");
}

async function getEvent(id) {
    return await useFetch(`${URL_EVENT}/${id}`, "GET");
}

async function postEvent (body) {
    return await useFetch(URL_EVENT, "POST", body);
}

async function patchEvent (id, body) {   
    return await useFetch(`${URL_EVENT}/${id}`, "PATCH", body);
}

async function deleteEvent (id) {
    return await useFetch(`${URL_EVENT}/${id}`, "DELETE");
}

export default { getEvents, getEvent, postEvent, patchEvent, deleteEvent };