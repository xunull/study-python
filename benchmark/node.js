
const moment = require('moment')

// 10000 * 10000
// 1515125560562
// 100000000
// 1515125560802
// 0.24

// 1515125610498
// 10000000000
// 1515125760461
// 149.963

count = 10000
let start = moment().valueOf()
console.log(start)
z = 0
for (let x = 0; x < count; x++) {
    for (let y = 0; y < count; y++) {
        z += 1
    }
}

let end = moment().valueOf()
console.log(z)
console.log(end)

let cost = end - start

console.log(`cost: ${cost} ms`)
