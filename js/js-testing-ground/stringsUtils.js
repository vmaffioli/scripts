function retirarAcentos(string) { 
    let mapaAcentosHex = {
        a: /[\xE0-\xE6]/g,
        e: /[\xE8-\xEB]/g,
        i: /[\xEC-\xEF]/g,
        o: /[\xF2-\xF6]/g,
        u: /[\xF9-\xFC]/g,
        c: /\xE7/g,
        n: /\xF1/g
    };
    for (let letra in mapaAcentosHex) { //retira acentos
        let expressaoRegular = mapaAcentosHex[letra]
        string = string.replace(expressaoRegular, letra)
    }
    return string 
}

function splitCustom(string) { //split sem posicoes vazias
    let result = []
    string.split(" ").forEach(element => {
        if (element.length > 0) {
            result.push(element)
        }
    })

    return result
}