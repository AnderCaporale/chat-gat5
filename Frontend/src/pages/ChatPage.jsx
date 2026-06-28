import { useState } from 'react';
import MessageList from '../components/MessageList';
import ChatInput from '../components/ChatInput';
import { chatService } from '../services/chatService';
import './ChatPage.css';

function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userId] = useState(() => `user-${Date.now()}-${Math.random().toString(36).substring(2, 11)}`);

  const handleSendMessage = async (messageText) => {
    const userMessage = {
      text: messageText,
      sender: 'user'
    };
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await chatService.sendMessage(messageText, userId);

      const assistantMessage = {
        text: response,
        sender: 'assistant'
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage = {
        text: 'Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente.',
        sender: 'assistant'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-page">
      <MessageList messages={messages} isLoading={isLoading} />
      <ChatInput onSend={handleSendMessage} disabled={isLoading} />
    </div>
  );
}

export default ChatPage;
