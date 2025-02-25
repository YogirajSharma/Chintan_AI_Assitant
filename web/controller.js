$(document).ready(function () { // Ensures the script runs only after the document is fully loaded



    // 🟢 Function to display assistant messages dynamically
    eel.expose(DisplayMessage)// Expose function to be called from Python (Eel)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message); // Update first <li> inside .siri-message with the assistant's text
        $('.siri-message').textillate('start'); // Animate the message using Textillate.js

    }

     // 🟢 Function to show the default UI (Oval shape) and hide Siri-like animation
    eel.expose(ShowHood) // Expose function to Python
    function ShowHood() {
        $("#Oval").attr("hidden", false); // Show the main UI
        $("#SiriWave").attr("hidden", true); // Hide the Siri wave animation
    }
     // 🟢 Function to display user messages in the chatbox
    eel.expose(senderText) // Expose function to Python
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");// Get chat box container
        if (message.trim() !== "") { // Ensure message is not empty
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // 🟢 Auto-scroll to the latest message
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }
    // 🟢 Function to display assistant's response in the chatbox
    eel.expose(receiverText)// Expose function to Python
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");// Get chat box container
        if (message.trim() !== "") {// Ensure message is not empty
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
             // 🟢 Auto-scroll to the latest message
            chatBox.scrollTop = chatBox.scrollHeight;

            // Hide Siri wave after message is added
            $("#SiriWave").attr("hidden", true);
            $("#Oval").attr("hidden", false);
        }
            }
});