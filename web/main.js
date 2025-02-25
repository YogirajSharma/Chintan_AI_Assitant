$(document).ready(function () {

    //eel.init()()
     // 🟢 Apply animation to text elements using Textillate.js
    $('.text').textillate({
        loop: true, // Animation will loop continuously
        sync: true, // Synchronize animation on all elements
        in: {
            effect: "bounceIn", // Bounce-in effect for text appearance

        },
        out: {
            effect: "bounceOut", // Bounce-in effect for text appearance

        },

    });

    // 🟢 Initialize Siri-like wave animation using SiriWave.js
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"), // The HTML element for the animation
        width: 640, // Wave animation width
        height: 200,// Wave animation height
        style: "ios9",// Sets wave style to iOS 9-like animation
        amplitude: "1.5",// Wave height intensity
        speed: "0.60",// Animation speed
        autostart: true,// Starts automatically when the page loads
      });

     // 🟢 Apply animation to Siri message
    $('.siri-message').textillate({
        in: {
            effect: "bounceIn",// Makes the message bounce in when displayed
        },
    });

    // 🟢 Click event handler for the microphone button
    $("#MicBtn").click(function () { 
        eel.playAssistantSound() // Calls the Python function to play an assistant sound
        $("#Oval").attr("hidden", true);// Hides the main UI
        $("#SiriWave").attr("hidden", false);// Shows the Siri-style animation
        eel.allCommands()()// Calls the Python function to process voice commands
    });
    
    // 🟢 Keyboard shortcut (Cmd + J) to trigger assistant
    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {// Check if 'J' key is pressed with the Command (Meta) key
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false); // Attach event listener to listen for keyup events

    // 🟢 Function to send the message to the assistant
    function PlayAssistant(message) {

        if (message != "") { // Ensure the message is not empty

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message); // Send the message to the backend via Eel
            $("#chatbox").val("")// Clear input box after sending
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }
    // 🟢 Function to toggle the visibility of the microphone and send buttons
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);  // Show microphone button if input is empty
            $("#SendBtn").attr('hidden', true); // Hide send button
        }
        else {
            $("#MicBtn").attr('hidden', true); // Hide microphone button
            $("#SendBtn").attr('hidden', false);// Show send button
        }
    }

    // 🟢 Event listener for keyup event on the input field
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val(); // Get input value
        ShowHideButton(message) // Call function to toggle button visibility
    
    });
    
    // 🟢 Event listener for clicking the Send button
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()// Get input value
        PlayAssistant(message)// Send message to assistant
    
    });

    // 🟢 Event listener for pressing Enter in the input field
    $("#chatbox").keypress(function (e) {
        key = e.which; // Get pressed key code
        if (key == 13) { // Check if Enter key (key code 13) is pressed
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });


});