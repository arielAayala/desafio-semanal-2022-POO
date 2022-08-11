function anagrama(a,b){
    let cont = 0
    let lstA = []
    let lstB = []
    lstA.split(a)
    lstB.split(b)
    lstA.forEach(i => {
        if (i == lstB[lstA.indexOf(i)]){
            cont +=1
        }
    return (length(a)==cont && length(b)==cont)
    });
}

anagrama("lana","alan")