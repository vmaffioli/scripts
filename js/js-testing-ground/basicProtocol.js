  
  function getProtocol(){
    let player_name = ""
    let data =  new Date;
    let random = Math.floor(Math.random() * 1000)
    return data.getMilliseconds() + "0" + data.getDate()+("0" + (data.getMonth() + 1)).substr(-2)+data.getFullYear()+Math.floor(1000 + Math.random() * 9000) + player_name;

  }

  console.log(protocol)