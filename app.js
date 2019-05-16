const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('hello my guy');
});

app.get('/api/random', (req, res) => {
    var arr = [0];
    for (i = 0; i <= 10; i++){
        arr.push(Math.floor((Math.random() * 100) + 1));
    }
    res.send(arr);
});

const port = process.env.PORT || 9876;
app.listen(port, () => console.log(`Listening of port ${port}...`))