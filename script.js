const chatWindow = document.getElementById("chatWindow");
const userInput = document.getElementById("userInput");
const debugToggle = document.getElementById("debugToggle");

function appendMessage(sender, message) {
  const bubble = document.createElement("div");
  bubble.className = sender === "user" ? "text-end mb-2" : "text-start mb-2";
  bubble.innerHTML = `
    <div class="d-inline-block p-2 rounded ${sender === "user" ? "bg-primary text-white" : "bg-light"}">
      ${message}
    </div>
  `;
  chatWindow.appendChild(bubble);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage("user", message);
  userInput.value = "";

  fetch("http://localhost:5005/webhooks/rest/webhook", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sender: "user", message })
  })
    .then(res => res.json())
    .then(data => {
      data.forEach(res => {
        appendMessage("bot", res.text);
        if (debugToggle.checked) console.log("Bot:", res);
      });
    })
    .catch(err => {
      appendMessage("bot", "⚠️ Server error or Rasa is not running.");
      console.error(err);
    });
}

function clearChat() {
  chatWindow.innerHTML = "";
}

function newAnalysis() {
  clearChat();
  appendMessage("bot", "🧠 Starting a new analysis... How can I assist you?");
}
