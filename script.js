async function sendToBackend() {
    // 1. Grab what the user typed
    const text = document.getElementById('userInput').value;
    const display = document.getElementById('responseArea');

    display.innerHTML = "Thinking..."; // Give visual feedback

    try {
        // 2. Call your Render URL (or localhost if testing)
        // Note: Change this to your actual Render URL later!
        const response = await fetch(`http://127.0.0.1:8000/ask?query=${text}`);
        
        // 3. Convert the response to JSON
        const data = await response.json();

        // 4. Update the HTML page with the answer
        display.innerHTML = `<p><strong>AI says:</strong> ${data.answer}</p>`;
    } catch (error) {
        display.innerHTML = "Error connecting to API.";
        console.error(error);
    }
}