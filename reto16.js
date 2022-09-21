class Mayus{

    ponerMayus(str){
        str = (str.split(" ")).map(function(i){return (i.replace(i[0],(i[0]).toUpperCase()))}).join(" ")
        console.log(str)
    }

}

let texto = new Mayus
texto.ponerMayus("hola mundo")