let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;

    setInterval(count, 1000);
});


// <!-- <!DOCTYPE html>
// <html lang="en">
//     <head>
//         <title>Hello</title>
//         <script>
//             function hello () {
//                 alert('Hello, world.');
//             }
            
//         </script>
//     </head>
//     <body>
//         <h1>Hello</h1>
//         <button onclick="hello()">Click</button>
//     </body>
// </html> -->
// <!-- ---------------------------------------------- -->

// <!DOCTYPE html>
// <html lang="en">
//     <head>
//         <title>Counter</title>
//         <script src="learning.js"></script>
//     </head>
//     <body>
//         <h1>0</h1>
//         <button>Count</button>
//     </body>
// </html>
// <!-- ---------------------------------------------- -->

// <!-- <!DOCTYPE html>
// <html lang="en">
//     <head>
//         <title>Hello</title>
//         <script>
//             function hello () {
//                 const heading = document.querySelector('h1');
//                 if (heading.innerHTML === 'Hello') {
//                     heading.innerHTML = 'Goodbye';
//                 } else {
//                     heading.innerHTML = 'Hello';
//                 }
//             }
            
//         </script>
//     </head>
//     <body>
//         <h1>Hello</h1>
//         <button onclick="hello()">Click</button>
//     </body>
// </html> -->