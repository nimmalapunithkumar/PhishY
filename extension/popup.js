function classifyText() {
    var text = document.getElementById("textInput").value;
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { text: text }, function(response) {
            document.getElementById("textResult").innerHTML = `<p>${response.text_result}</p>`;
        });
    });
}

// Automatically classify the current URL and display above text input on popup load
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'classifyURL' }, function(response) {
        document.getElementById("urlResult").innerHTML = `<p>${response.url_result}</p>`;
    });
});
