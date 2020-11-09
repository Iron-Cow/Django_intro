console.log('Hello world!');
// alert('Hello world 2');
// alert({'legs': 3});


// ---------------------

function example() {
    // демонстрационный пример
    alert('Hello, JavaScript');
    let name = 'Yura';
    // const number = 1;
    // number = 2;  ERROR

    // варианты создания переменных
        // let
        // var
        // conts

    alert('Hello ' + name);
    let pseudo = prompt('Input pseudonim');
    alert('Pseudonim -> ' + pseudo)

    if (pseudo === ''){
        window.location = 'http://bing.com'
    }else{
        alert(pseudo + ' добро пожаловать!')
    }

}

// example();
// ----------------------

$(document).ready(function () {
    console.log('ready works');

    $('#login_field').click(function () {
        alert("ВНИМАНИЕ!!! КЛИК ПО ЛОГИНУ!!!")
    })
})

