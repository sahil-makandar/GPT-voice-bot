// Check for browser compatibility for SpeechRecognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  alert("Sorry, your browser does not support speech recognition.");
}

const recognition = new SpeechRecognition();
recognition.lang = "en-US";
recognition.interimResults = false;

const speakBtn = document.getElementById("speakBtn");
const conversationDiv = document.getElementById("conversation");

// Function to append messages to the conversation div
function appendMessage(sender, text) {
  const p = document.createElement("p");
  p.className = "message " + sender;
  p.textContent = `${sender === "user" ? "You" : "Bot"}: ${text}`;
  conversationDiv.appendChild(p);
}

// Function to use text-to-speech to speak out the bot's answer
function speakText(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "en-US";
  speechSynthesis.speak(utterance);
}

// Start voice recognition when the button is clicked
speakBtn.addEventListener("click", () => {
  recognition.start();
});

recognition.addEventListener("result", (event) => {
  const transcript = event.results[0][0].transcript;
  appendMessage("user", transcript);
  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: transcript })
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        appendMessage("bot", "Error: " + data.error);
      } else {
        appendMessage("bot", data.answer);
        speakText(data.answer);
      }
    })
    .catch(error => {
      appendMessage("bot", "Error: " + error);
    });
});

recognition.addEventListener("error", (event) => {
  appendMessage("bot", "Speech recognition error: " + event.error);
});
