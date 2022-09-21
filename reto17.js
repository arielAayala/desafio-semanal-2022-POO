class Carrera{
    constructor(pista){
        this.pista = pista.split("")
    }

    validarCarrera(acciones){
        let i = 0
        while(i < this.pista.length){
            if(acciones[i]=="jump" && this.pista[i]== "-"){
                this.pista[i] = "x"
            }else if (acciones[i]== "run" && this.pista[i] == "|"){
                this.pista[i] ="/"
            }
            i +=1
        }
        console.log(this.pista)
        return !((this.pista.includes("/")) || (this.pista.includes("x")))
    }
}

let corredor = new Carrera("-|-|--|")
console.log(corredor.validarCarrera(["run","jump","run","jump","run","run","jump"]))