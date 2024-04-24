function getElenco() {
    fetch()
    .then(data => {
        document.getElementById('elenco').innerHTML = data
        console.log(data)
        for(let regione in data) {
            document.getElementById('elenco').innerHTML = data
        }
    })
}