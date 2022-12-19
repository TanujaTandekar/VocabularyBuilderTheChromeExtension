
// document.getElementById("btn").addEventListener("click", myfunction);
// function myfunction() {
//     console.log("Abhi")
//     // window.location.href = "ind.html";
//     window.location.replace("./templates/ind.html")
// }


const resultDiv = document.querySelector(".result");
const defDiv = document.querySelector(".def");
const wordEle = document.querySelector(".word");
const phonetics = document.querySelector(".phonetics");
const audio = document.querySelector("audio");
const wordMeaning = document.querySelector(".word-definition");
const example = document.querySelector(".example");
// const synonyms = document.querySelector(".synonyms .pills");

fetch('http://6688-103-80-117-206.ngrok.io')
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        var t = myJson['word'];
        document.getElementById('ppp').innerHTML = t;
    })

var handle = function () {
    document.addEventListener('keydown', async (e) => {
        let key = e.key;
        var word = e.target.value;
        if (key == 'Enter') {
            const result = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
            const data = await result.json();
            defDiv.style.display = "block";
            if (result.ok) {
                wordEle.innerText = data[0].word;
                phonetics.innerText = data[0].phonetics[0].text;
                audio.src = data[0].phonetics[0].audio;
                wordMeaning.innerText = data[0].meanings[0].definitions[0].definition;
                example.innerText = data[0].meanings[0].definitions[0].example;
                if(example.innerText == 'undefined')
                example.innerText = 'No examples found'
                return;
            }
        }
    });
};

// document.getElementById("inp").addEventListener("keypress", handle(event));
document.addEventListener("DOMContentLoaded", async (e) => {
    handle();
}
);
