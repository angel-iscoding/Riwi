import useFetch from "./utils/fetch.js";

const URL = "http://localhost:3000/categories"

async function getCategories() {
    return await useFetch(URL, "GET")
}

async function postCategory(body) {
    return await useFetch(URL, "POST", body);
}

export default { getCategories , postCategory}