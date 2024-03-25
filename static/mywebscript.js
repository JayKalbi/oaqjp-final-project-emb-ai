let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                console.error("Error:", xhttp.status, xhttp.statusText);
            }
        }
    };
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify({textToAnalyze: textToAnalyze}));
}
