


// function enviarEmail(para, id, assunto, texto) {
//     //lib to send email
//     console.log(para, id, assunto, texto);
// }

// class EnviarEmailUsuario {

//     send() {
//         enviarEmail("vini@gmail.com", 9899, "olá!", "tudo bem?");
//     }
// }

interface DadosDeEnvioEmail {
    para: string;
    id: string;
    assunto: string;
    texto: string;
}

function enviarEmail({para, id, assunto, texto}: DadosDeEnvioEmail) {
    console.log(para, id, assunto, texto)
}
 
class EnviarEmailParaUsuario {
    send() {
        enviarEmail({
            para: "dani@gmail.com",
            id: "9899",
            assunto: "Olá",
            texto: "Tudo bem?"
        })
    }
}