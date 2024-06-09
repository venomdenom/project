document.getElementById('sendBtn').addEventListener('click', sendText);

function sendText() {
    const text = document.getElementById('textInput').value;
    document.getElementById('sentText').innerText = `Отправленный текст: ${text}`; // Отображаем отправленный текст
    fetch('http://127.0.0.1:5000/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.result;
    })
    .catch(error => {
        console.error('Произошла ошибка:', error);
    });
}
