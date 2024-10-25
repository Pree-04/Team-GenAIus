import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { IconButton, CircularProgress } from '@mui/material';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import LightModeIcon from '@mui/icons-material/LightMode';
import SendIcon from '@mui/icons-material/Send';

const Chatbot = () => {
  const [chatHistory, setChatHistory] = useState([]);
  const [currentChat, setCurrentChat] = useState(0);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [loading, setLoading] = useState(false); // Added loading state
  const chatEndRef = useRef(null);

  const welcomeMessage = "Greetings! I'm GenAIus KT, your Onboarding Buddy. How can I assist you?";

  useEffect(() => {
    document.body.className = isDarkMode ? 'dark' : 'light';
    if (messages.length === 0 && chatHistory.length === 0) {
      setMessages([{ sender: 'bot', text: welcomeMessage, logo: true }]);
    }
  }, [isDarkMode]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (input.trim() === '') return;

    setMessages((prevMessages) => [...prevMessages, { sender: 'user', text: input }]);
    setLoading(true); // Set loading to true

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/chat', { message: input });
      setMessages((prevMessages) => [
        ...prevMessages, 
        { sender: 'bot', text: response.data.reply, logo: true }
      ]);
    } catch (error) {
      console.error('Error:', error);
      setMessages((prevMessages) => [...prevMessages, { sender: 'bot', text: 'Something went wrong.', logo: false }]);
    } finally {
      setLoading(false); // Set loading to false after response
    }

    setInput('');
  };

  const toggleTheme = () => {
    setIsDarkMode((prevMode) => !prevMode);
  };

  const handleNewChat = () => {
    window.location.reload(); // Reloads the page
  };

  const selectChat = (index) => {
    setMessages(chatHistory[index]);
    setCurrentChat(index);
  };

  return (
    <div className="container">
      <div className="left-panel">
        <h2>GenAIus KT</h2>
        <button className="new-chat" onClick={handleNewChat}>+ New Chat</button>
        
        <hr className="divider" />

        <ul className="chat-history">
          {chatHistory.map((_, index) => (
            <li key={index} onClick={() => selectChat(index)}>Chat Message {index + 1}</li>
          ))}
        </ul>
      </div>
      <div className="chatbot-container">
        <div className="header">
          <span className="TitleHeader">
            <img src="/logo.png" alt="Chatbot Logo" className="header-logo" />
            <h1>GenAIus KT</h1>
          </span>
          <IconButton onClick={toggleTheme} style={{ color: isDarkMode ? '#ffc107' : '#000' }}>
            {isDarkMode ? <LightModeIcon /> : <DarkModeIcon />}
          </IconButton>
        </div>

        <div className="chat-window">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender} ${isDarkMode ? 'dark' : 'light'}`}>
              {msg.logo && <img src="/logo.png" alt="Chatbot Logo" className="bot-logo" />}
              <span dangerouslySetInnerHTML={{ __html: msg.text }} />
            </div>
          ))}
          {loading && (
            <div className="loading-message">
              <CircularProgress size={24} />
              <span className="loading-text">Working On It...</span>
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="input-container">
          <input
            type="text"
            className={isDarkMode ? 'dark' : 'light'}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          />
          <IconButton onClick={handleSend} style={{ color: isDarkMode ? '#ffc107' : '#246ffe' }}>
            <SendIcon />
          </IconButton>
        </div>
      </div>

      <style jsx>{`
        .container {
          display: flex;
          height: 100vh;
          width: 100vw;
        }

        .left-panel {
          width: 20%;
          background-color: var(--sidebar-bg);
          padding: 20px;
          border-right: 1px solid var(--border-color);
          display: flex;
          flex-direction: column;
        }

        .left-panel h2 {
          font-size: 1.5rem;
          margin-bottom: 20px;
        }

        .new-chat {
          background-color: #246ffe;
          border: none;
          padding: 10px;
          margin-bottom: 20px;
          cursor: pointer;
          border-radius: 8px;
          color: #fff;
          font-size: 1rem;
          box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
          transition: background-color 0.3s ease;
        }

        .new-chat:hover {
          background-color: #205ce4;
        }

        .divider {
          border: 0;
          height: 1px;
          background-color: var(--border-color);
          margin: 20px 0;
        }

        .chat-history {
          list-style: none;
          padding: 0;
        }

        .chatbot-container {
          width: 80%;
          display: flex;
          flex-direction: column;
          background-color: var(--background-color);
          padding: 20px;
          overflow: hidden;
        }

        .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 10px;
        }

        .TitleHeader {
          display: flex;
          align-items: center; /* Align logo and title vertically */
        }

        .header-logo {
          width: 40px; /* Adjust size as needed */
          height: 40px; /* Adjust size as needed */
          object-fit: cover;
          border-radius: 50%;
          margin-right: 10px; /* Add some space between logo and title */
        }

        h1 {
          font-size: 1.5rem; /* Adjust font size as needed */
          margin: 0; /* Remove default margin */
        }

        .chat-window {
          flex: 1;
          overflow-y: auto;
          margin-bottom: 10px;
          background-color: var(--chat-background-color);
          padding: 10px;
          border-radius: 10px;
          display: flex;
          flex-direction: column;
          box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
        }

        .message {
          padding: 12px;
          margin: 8px 0;
          border-radius: 18px;
          max-width: 60%;
          word-wrap: break-word;
          display: flex;
          align-items: center;
          box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
          transition: background-color 0.3s ease;
        }

        .message.user {
          text-align: right;
          align-self: flex-end;
          background-color: #246ffe;
          color: white;
          border-radius: 18px 18px 0 18px;
        }

        .message.bot {
          text-align: left;
          align-self: flex-start;
          background-color: #f1f1f1;
          color: black;
          border-radius: 18px 18px 18px 0;
        }

        .bot-logo {
          width: 30px;
          height: 30px;
          object-fit: cover;
          border-radius: 50%;
          margin-right: 10px;
        }

        .input-container {
          display: flex;
          align-items: center;
          border-top: 1px solid var(--border-color);
          padding: 10px 0;
        }

        input {
          flex: 1;
          padding: 12px 16px;
          border-radius: 30px;
          border: 1px solid var(--border-color);
          font-size: 1rem;
          margin-right: 10px;
        }

        input.light {
          background-color: white;
          color: black;
        }

        input.dark {
          background-color: #3c3c3c;
          color: white;
        }

        .loading-message {
          display: flex;
          align-items: center;
          margin-top: 10px;
        }

        .loading-text {
          margin-left: 8px; /* Adjust the value to increase or decrease the space */
        }
      `}</style>
    </div>
  );
};

export default Chatbot;
