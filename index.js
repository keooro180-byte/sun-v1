async function sendMessage() {
    const input = document.getElementById('user-input');
    const output = document.getElementById('output');
    const message = input.value.trim();

    if (message) {
        output.innerHTML += `<div class="user-msg">أنت: ${message}</div>`;
        input.value = '';

        try {
            const response = await fetch('/.netlify/functions/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            const sunReply = data.reply || "لم يتم استلام رد";

            output.innerHTML += `<div class="sun-msg">[SUN]: ${sunReply}</div>`;
        } catch (err) {
            output.innerHTML += `<div class="error">⚠️ خطأ: ${err.message}</div>`;
        }
        output.scrollTop = output.scrollHeight;
    }
}
