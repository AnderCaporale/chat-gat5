import './ChatMessage.css';

function ChatMessage({ message, sender }) {
  const isUser = sender === 'user';

  return (
    <div className={`message-container ${isUser ? 'user' : 'assistant'}`}>
      <div className={`message-bubble ${isUser ? 'user-bubble' : 'assistant-bubble'}`}>
        {message}
      </div>
    </div>
  );
}

export default ChatMessage;
