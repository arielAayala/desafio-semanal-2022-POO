
class Fechas{
    defirenciaFechas(fecha1,fecha2){
        fecha1 = fecha1.split("/")
        fecha2 = fecha2.split("/")

        const  date1 = new Date(fecha1[1] +'/'+ fecha1[0]+ "/"+fecha1[2]);
        const date2 = new Date(fecha2[1] +'/'+ fecha2[0]+ "/"+fecha2[2]);
        const difDias = (Math.abs(date2 - date1) / (1000 * 60 * 60 * 24));
        if(isNaN(difDias)){
            throw "fechas no validas"
        } else{
            return difDias
        }
        
    }
}

let fechas = new Fechas
console.log(fechas.defirenciaFechas("29/2/2020","20/2/2020"))



