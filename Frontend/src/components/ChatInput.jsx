import { useState } from 'react';
import './ChatInput.css';

function ChatInput({ onSend, disabled }) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && !disabled) {
      onSend(inputValue.trim());
      setInputValue('');
    }
  };

  return (
    <form className="chat-input-container" onSubmit={handleSubmit}>
      <input
        type="text"
        className="chat-input-field"
        placeholder="Digite sua mensagem..."
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        disabled={disabled}
      />
      <button
        type="submit"
        className="chat-send-button"
        disabled={disabled || !inputValue.trim()}
      >
        Enviar
      </button>
    </form>
  );
}

export default ChatInput;
