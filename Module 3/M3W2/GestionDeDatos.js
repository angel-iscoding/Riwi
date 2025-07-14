//Inicializacion de proyecto

console.log("¡Gestión de Datos con Objetos, Sets y Maps!")

//Definire el objeto de producto

const productos = {
    1: { id: 1, nombre: "Laptop", precio: 1500 },
    2: { id: 2, nombre: "Mouse", precio: 25 },
    1: { id: 3, nombre: "Teclado", precio: 50 },   
}

console.log("Ojectos products: ", productos)

//Crear un Set con los nombres de los productos
const setProductos = new Set(Object.values(productos).map(producto => producto.nombre));
console.log("Set de productos únicos:", setProductos)

//Crear un Ma para agregar categorías a los productos
const mapProductos = new Map([
    ["Electronica", "Laptop"],
    ["Accesorios", "Mouse"],
    ["Accesorios", "Teclado"]
]);

console.log("Map de productos y categorias", mapProductos);

for (const id in productos) {
    console.log(`Producto ID: ${id}, Detalles:`, productos[id]);
}

for (const producto of setProductos) {
    console.log("Producto único:", producto);
}

mapProductos.forEach((producto, categoria) => {
    console.log(`Categoría: ${categoria}, Producto: ${producto}`);
});

console.log("Pruebas completas de gestión de datos:");
console.log("Lista de productos (Objeto):", productos);
console.log("Lista de productos únicos (Set):", setProductos);
console.log("Categorias y productos (Map):", mapProductos);



