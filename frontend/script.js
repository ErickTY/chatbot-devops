// script.js
async function send() {
  const input = document.getElementById("userInput").value;
  const res = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "seutoken123"
    },
    body: JSON.stringify({ message: input })
  });
  const data = await res.json();
  document.getElementById("response").innerText = data.response;
}
