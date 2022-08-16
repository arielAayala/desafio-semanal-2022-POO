function anagrama(a,b){
    let cont = 0
    let igual = 0
    if (a.lenght == b.lenght && a != b){
        let lstA = (a.split("")).sort()
        let lstB = (b.split("")).sort()
        lstA.forEach(i => {
        if (i == lstB[cont]){
            igual +=1}
        cont +=1});  
    }
    return (b.length==igual && a.length==igual)
}
console.log(anagrama("lena","alan")) 