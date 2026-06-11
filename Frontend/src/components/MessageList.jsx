import { useEffect, useRef } from 'react';
import ChatMessage from './ChatMessage';
import './MessageList.css';

function MessageList({ messages, isLoading }) {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="message-list-container">
      {messages.length === 0 && (
        <div className="empty-state">
          <p>Olá! Como posso ajudar você hoje?</p>
        </div>
      )}
      {messages.map((msg, index) => (
        <ChatMessage
          key={index}
          message={msg.text}
          sender={msg.sender}
        />
      ))}
      {isLoading && (
        <div className="loading-indicator">
          <span>Digitando...</span>
        </div>
      )}
      <div ref={messagesEndRef} />
    </div>
  );
}

export default MessageList;
