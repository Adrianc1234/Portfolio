# DATA BASE (JavaScript)
## Introduction.
This is a project where we can see how a basic Data Base works in JavaScript. this Data Base has these functions: `Read`, `Edit`, `Delete`, `update`. It is a basic way to make a Data Base and is a good way to start with JavaScript and understand the functional programming and how java works.

_**You can run this code here:**_[_Compiler_](https://playcode.io/466577?tabs=script_DataBase.js,preview,console).

## Code.
For the first part you can see that we declared a clas with the name `Persona`, after that we use the function `constructor` that it allows us to assign the values that we will use like properties for Persona class, in this case the properties and the values that we use are lists with the names: `nombre`,`edad` and `dir`. 

The assignments were `this.name = nombre`, `this.age = edad` and `this.ip = dir`.
````JavaScript
//EDITAR
class Persona {
  constructor (nombre, edad, IP) {
    this.name = nombre;
    this.age = edad;
    this.ip = IP;
  }
}
````
````JavaScript
//The lists:
var names = ['Adrian', 'Liss','Hector'];
var edad = [19,15,16];
var IP = [124,123,125];
````
The way to write this code was on this way. As you can see for the first part we use `get name()` function to write the name that we will use when we call that property, also inside of _get()_ we need to write what it will do and we can call many functions that we already declared inside of the _get()_ and then we call it in this way: _**user.nameofmyget()**_; user is a variable that before you need to declare like `user = new persona(name,edad,IP)`
_**(Example) It is not part for the code:**_
````JavaScript
  // get data for one person and only wrote to give a example.
  // in this case if we write (user.datos) and suppose that we only have one data for each list.
  // it will print all his data.
  get  datos ()   {
     return this.obtener_datos(); // the function that i want to return its result.
   }
  // Método nombre
  obtener_datos () { // my function for  the example
    return this.name;
    return this.edad;
    return this.IP;
  }
````
## Methods and their names for the `get name()`.
_**Names for `get()` :**_
````JavaScript
// get the average ages.
  get   promedio  ()   {
     return this.mean();
   }
//read all data base.
  get Datos () {
    return this.lecture();
  }
// add a person.
  get addition() {
    return this.add();
  }
//edit one data.
  get edit() {
    return this.editing()
  }
//update the ages.
  get update() {
    return this.act();
  }
````
_**Methods:**_
1- This method called `mean()` is to make a mathematical operation to calculate the Average age and we use `for(i=0 ; i < 3; i++){instructions}` to get each value inside of the edad list and we make a sum for all values and we divide the sum over the lenght of the list.
````JavaScript
  // Método
  mean () {
    var i;
     var prome = 0;
     for(i=0 ; i < 3; i++){
      prome = prome + edad[i]
      prome = prome / 5
     }
     console.log("This is the mean of the Ages: "+ prome)
  }
````
2- This method is to read all data inside of the data base and for that we used the same method beacuse all data for each person are in the same position, then when the counter `i` change, we call the data in all lists in that position with this way: `name_list[i]`.
````JavaScript
//metodo de lectura de todos los datos
  lecture () {
    var i;
    for(i = 0; i < 3; i++) {
    console.log("Estos son los datos de " + names[i] + ": " )
    console.log("name: " + names[i])
    console.log("edad: " + edad[i])
    console.log("IP:" + IP[i]+"\n")
    }
  }
````
3-This method called `del()` uses the function `.splice()` but to use this function you need to know that it is written like _**namelist.splice(position, amount of values that you want delete)**_ .
````JavaScript
  // Método eliminar
  del (val) {
    var pos = names.indexOf(val);
    names.splice(pos,1)
    console.log("Nombres: " + names)
    edad.splice(pos,1)
    console.log("Edades" + edad)
    IP.splice(pos,1)
    console.log("IP:" + IP)
  }
 ````
 4- This method is to add some person and all about him or her, we use the function `.unshift()` to assign the value that we want to add, As we want to add all about that person, then we applythis function for each list with the variable inside of the function.
 ````JavaScript
  //funcion añadir
  add() {
    names.unshift(N_name);
    edad.unshift(N_age);
    IP.unshift(N_ip);
    console.log("ASI ESTA LA BASE DE DATOS")
    console.log("Lista de nombres: "+ names)
    console.log("Lista de IP: " + IP)
    console.log("Lista de edades: " + edad)
  }
 ````
 5- This method is to edit some data of some person, we only get the name of the person that we need to edit and we use the `.indexOf()` to get the position on the list where the person is, then whe call all values for each list to check its values and change some using this way: 
 _**name_lis[position]=new_value**_
 ````JavaScript
  //metodo de edicion
  editing(){
    console.log("Esta es la persona que deseas editar: "+ N_dname)
    pos = names.indexOf(N_dname)
    names[pos] = N_dname
    edad[pos] = N_dage
    IP[pos] = N_dip
    console.log("LOS NUEVOS DATOS DE "+ N_dname+" SON: ")
    console.log("Nombre: " + names[pos])
    console.log("Edad: " + edad[pos])
    console.log("IP: " + IP[pos])
  }
 ````
 6-This Method is only to add years for the Ages, it uses a `for` As in previous and we make a sum for each Age and we add the result inside of a empty list called `var list = []` and we match this list with the precious list and we use `.reverse()` function to put in order the data.
 ````JavaScript
  //funcion para actualizar edades
  act() {
    var list = []
    console.log("Edades actuales: " + edad)
    edad.forEach(function(element) {
    var new_a = element + years;
    list.unshift(new_a);
    });
    edad = list
    edad = edad.reverse()
    console.log("Estos son las nuevas edades al pasar "+ years + " años: ")
    console.log(edad)
  } 
````
## Calls
These are the ways to call all functions using the names of the `get name()` that we assigned and declaring what variables it will use or what values:
````JavaScript
//ver el promedio
console.log("mean:" + user.promedio +"\n")

//ver a las personas en la base de datos
console.log(user.Datos)

//eliminar a persona en la base de datos Var
//nombre que queremos borrar
var val = 'Adrian'; 
console.log("RESULTADOS DE LA ELIMINACION")
console.log(user.elimination)

//agregar a persona
var N_name = 'luis';
var N_age = 12;
var N_ip = 124
console.log("RESULTADOS DE LA AGREGACION.")
console.log(user.addition)

//editar un dato en especifico
var N_dname = "Luis";
var N_dage= 21;
var N_dip = 2001;
console.log("EDICION DE UN DATO")
console.log(user.edit)

//actualizar edades si ya paso un año
console.log("ACTUALIZACION DE EDADES")
var years = 2;
console.log(user.update)
````
