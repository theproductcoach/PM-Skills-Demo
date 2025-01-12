import React, { useState } from 'react';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  const handleSend = async () => {
    // 1) Add user’s message to the local chat
    const newMessages = [...messages, { role: 'user', content: userInput }];
    setMessages(newMessages)
      // 2) Make a POST request to the server
  try {
    const response = await fetch('http://localhost:3001/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    // 3) Append the server response to the chat
    const updatedMessages = [
      ...newMessages,
      { role: 'assistant', content: data.answer },
    ];
    setMessages(updatedMessages);
  } catch (error) {
    console.error('Error calling /api/chat:', error);
  }

  // 4) Clear the input field
  setUserInput('');
};

return (
  <div
    className="d-flex justify-content-center align-items-center"
    style={{ minHeight: "100vh", backgroundColor: "lightblue" }}
  >
    {/* 
        Use a wide width class (w-75) or set a style with maxWidth/minWidth 
        to control how big it gets on large screens.
        You can tweak w-75 -> w-50, etc., or add style={{ maxWidth: '1000px' }}.
      */}
    <div
      className="card shadow-sm w-75"
      style={{ maxWidth: "1000px", backgroundColor: "white" }}
    >
      <div className="card-body">
        <h2 className="card-title text-center mb-4">Find Similar Documents</h2>
        <div
          className="mb-3 border rounded p-3"
          style={{ minHeight: "300px", maxHeight: "400px", overflowY: "auto" }}
        >
          {messages.map((msg, i) => {
            const isUser = msg.role === "user";
            return (
              <div
                key={i}
                className={`mb-2 p-2 rounded ${
                  isUser ? "bg-primary text-white" : "bg-light"
                }`}
                style={{
                  maxWidth: "80%",
                  marginLeft: isUser ? "auto" : "0",
                }}
              >
                <strong>{msg.role}:</strong> {msg.content}
              </div>
            );
          })}
        </div>

        <div className="input-group">
          <input
            type="text"
            className="form-control"
            placeholder="Type your message..."
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") handleSend();
            }}
          />
          <button className="btn btn-primary" onClick={handleSend}>
            Send
          </button>
        </div>
      </div>
    </div>
  </div>
);
}

export default Chat;
