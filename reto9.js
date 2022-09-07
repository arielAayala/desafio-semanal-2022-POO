let expresion = "{[3+4(1/2)]*2}"

function verificarExpresion(text){
    let cont = 0
    for (let i of text) {
        if(i == "{" || i == "[" || i == "("){
            cont +=1
        }else if(i == "}" || i == "]" || i == ")"){
            cont -=1
        }
    }
    console.log(cont)
    return (cont == 0)
}


console.log(verificarExpresion(expresion))

/*arreglar los retos 9*/