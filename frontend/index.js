function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

async function askGemini() {
    const SERVER_DOMAIN = 'http://127.0.0.1:5000'

    const crashData = localStorage.getItem("crashData")

    console.log(crashData)
    
    if (!crashData) {
        console.log("data does not exist")
        return
    }

    const response = await fetch(`${SERVER_DOMAIN}/askGemini`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: crashData
    })

    console.log(response)
}