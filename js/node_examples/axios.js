const axios = require('axios') 

const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemon}`)
const api = await response
const data = api.data

