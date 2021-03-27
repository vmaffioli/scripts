import express from 'express';

const app = express();

/**
 * GET => BUSCA
 * POST => SALVAR
 * PUT => ALTERAR
 * DELETE => DELETAR
 * PATCH => ALTERAÇÃO ESPECÍFICA
 */

 // http://localhost:3333/users
app.get("/", (request, response) => {
    return response.send("Hello Word - NLW04")
})

// 1 param => Rota(recurso api)
// 2 param => Request, response
app.post("/", (request, response) => {
    //Recebeu os dados para salvar
    return response.send("Os dados foram salvos com sucesso!")
})

app.listen(3333, () => console.log("Server is running"));

