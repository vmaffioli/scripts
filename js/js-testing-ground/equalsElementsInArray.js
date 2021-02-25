function analyzeMemories(recognizingSomething) { //analisa lista de itens reconhecidos
    let thingsList = [] 
    let alreadyRecognized = false

    for (let i = 0; i < recognizingSomething.length; i++) {
        const itemRecognized = recognizingSomething[i]

        for (let ii = 0; ii < thingsList.length; ii++) {
            const itemMemorized = thingsList[ii]

            if(itemMemorized===itemRecognized){
                alreadyRecognized=true
            }
            
        }
        
        if(alreadyRecognized){
          let prefixCounter = "%%"
          let counter = 0
            for (let ii = 0; ii < array.length; ii++) {
                const thing = thingsList[ii];
                
                if(thing===itemRecognized){
                  counter++

                  if(thing.substring(str.length-5,str.length-3===prefixCounter)){

                    if(str.substring(str.length-5,str.length-3)===prefixCounter){
  let numbers = parseInt(str.substring(str.length-3,str.length)) + 1

}


                  } else {

                    thingsList[ii] = thingsList[ii] + prefixCounter + counter

                  }
                    
                }
            }
            
        } else {
            counter++
            thingsList.push[itemRecognized]

        }
    }

    console.log(thingsList)
}



let list = [
  "idteste02%%001",
  "idteste01%%003",
  "idteste05%%009"

]

//console.log(recognizingSomething(list))

let str = "idteste02%%001"

//console.log(str.substring(0,str.length-5))
function getCounter(str){ //add validacao
  return parseInt(str.substring(str.length-3,str.length))
}

function recognizedMemory(array){
  let memoryCache
  for(let i=0;i<array.length;i++){
    if(memoryCache) {
      if(getCounter(array[i]) >= getCounter(memoryCache[0])){
        memoryCache.unshift(array[i])
      } else {
        memoryCache.push(array[i])
      }
    } else {
      memoryCache = []
      memoryCache.unshift(array[i])
    }

  }
  return memoryCache
}

//console.log(parseInt(list[0].substring(list[0].length-3,list[0].length)))
recognizedMemory(list)


