function solve(input) {
    const names = {}
    for (const line of input) {
        names[line] = line.length
    }

    for (const key in names) {
        console.log(`Name: ${key} -- Personal Number: ${names[key]}`);
    }
}

solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]
    )