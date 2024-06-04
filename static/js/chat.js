// static/js/chat.js
document.getElementById("messageForm").onsubmit = function (e) {
  e.preventDefault();
  const messageInput = document.getElementById("messageInput");
  const message = messageInput.value;
  const chatbox = document.getElementById("chatbox");

  if (message.trim() !== "") {
    const messageElement = document.createElement("span");

    // Cấu hình div
    messageElement.textContent = message;
    messageElement.classList.add("message");

    // Thêm style trực tiếp
    messageElement.style.backgroundColor = "black"; // Màu nền xanh nhạt
    messageElement.style.padding = "10px"; // Tăng padding
    messageElement.style.marginBottom = "10px"; // Tăng margin dưới
    messageElement.style.borderRadius = "15px";
    messageElement.style.maxWidth = "824px";
    messageElement.style.wordBreak = "break-word";
    messageElement.style.width = "fit-content";
    chatbox.appendChild(messageElement);
    messageInput.value = "";

    // Cuộn xuống cuối chatbox
    chatbox.scrollTop = chatbox.scrollHeight;
  }
};
