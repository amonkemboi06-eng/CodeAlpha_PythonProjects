const chatbox = document.getElementById("chatbox");
const input = document.getElementById("message");

// Send message when Enter is pressed
function handleKey(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

// Add a message bubble
function addMessage(text, sender) {
    const message = document.createElement("div");

    message.classList.add("message");
    message.classList.add(sender);

    message.textContent = text;

    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Show typing indicator
function showTyping() {
    const typing = document.createElement("div");
    typing.classList.add("typing");
    typing.id = "typing";

    typing.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;

    chatbox.appendChild(typing);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Remove typing indicator
function removeTyping() {
    const typing = document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}

// Send message to Flask
async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    // Display user message
    addMessage(message, "user");

    input.value = "";
    input.focus();

    // Show typing dots
    showTyping();

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // Simulate thinking time
        setTimeout(() => {

            removeTyping();

            addMessage(data.response, "bot");

        }, 700);

    } catch (error) {

        removeTyping();

        addMessage("Connection error.", "bot");
    }
}