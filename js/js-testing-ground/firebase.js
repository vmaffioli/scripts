
//config --> .env
const firebase = require("firebase");

var firebaseConfig = {
    apiKey: process.env.APIKEY,
    authDomain: process.env.AUTHDOMAIN,
    databaseURL: "",
    projectId: process.env.PROJECTID,
    storageBucket: process.env.STORAGEBUCKET,
    messagingSenderId: process.env.MESSAGINGSENDERID,
    appId: process.env.APPID,
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
//const database = firebase.database();



//push
try {
    database.ref("pathinfirebase/")
        .once('value').then(async function () {
            database.ref("pathinfirebase/")
                .set({
                    titulo: "xxx",
                    autores: "xxx",
                })
        })
} catch (error) {
    console.error(error)
}

//pull
try {
    database.ref(`favoraveis`).once('value', function (snapshot) {
        let data = []
        snapshot.forEach(
            function (ChildSnapshot) {
                data.push(ChildSnapshot.val())
            }
        )
    });
    next();
} catch (error) {
    console.error(error)
}