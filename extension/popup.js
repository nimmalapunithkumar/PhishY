document.addEventListener('DOMContentLoaded', function() {
    // Classify the current URL
    classifyURL();

    // Add event listener to the button
    document.getElementById('classifyTextBtn').addEventListener('click', function() {
        classifyText();
    });
});

function classifyURL() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var currentUrl = tabs[0].url;
        fetch('http://localhost:5000/classify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: currentUrl })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("urlResult").innerHTML = `<p>${data.url_result}</p>`;
            document.getElementById("currentUrl").innerHTML = `<p>Current URL: ${currentUrl}</p>`;
        })
        .catch(error => console.error('Error fetching URL:', error));
    });
}

function classifyText() {
    var text = document.getElementById("textInput").value;
    fetch('http://localhost:5000/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("textResult").innerHTML = `<p>${data.text_result}</p>`;
    })
    .catch(error => console.error('Error classifying text:', error));
}
