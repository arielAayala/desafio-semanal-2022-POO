function calculoPoligono(poli){
    let calculo = 0
    if(poli == "triangulo"){
        let alto = parseFloat(prompt("alto de" + poli))
        let ancho = parseFloat(prompt("ancho de" + poli))
        calculo = (alto * ancho)/2
    }else if(poli == "rectangulo"){
        let alto = parseFloat(prompt("alto de" + poli))
        let ancho = parseFloat(prompt("ancho de" + poli))
        calculo = alto * ancho
    }else if(poli == "cuadrado"){
        let lado = parseFloat(prompt("lado de" + poli))
        calculo = lado *4
    }else{
        console.log("error")
    }
    console.log("el area del "+poli+" es: "+calculo)
}
calculoPoligono("triangulo")