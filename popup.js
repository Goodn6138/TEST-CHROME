document.getElementById("fetchBtn").addEventListener("click", async () => {
  const responseEl = document.getElementById("response");
  responseEl.textContent = "Connecting...";
  try {
    const res = await fetch("http://127.0.0.1:8000/ping");
    const data = await res.json();
    responseEl.textContent = `Response: ${data.message}`;
  } catch (err) {
    responseEl.textContent = "Failed to connect.";
    console.error(err);
  }
});
