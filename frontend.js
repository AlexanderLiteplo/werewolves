import React, { useState, useRef, useEffect } from 'react';
import { Moon, Sun } from 'lucide-react';

// Mock data for our game state
const MOCK_PLAYERS = [
  { id: 1, name: 'Claude-1', role: 'werewolf', isAlive: true, avatar: '/api/placeholder/40/40' },
  { id: 2, name: 'GPT-4', role: 'villager', isAlive: true, avatar: '/api/placeholder/40/40' },
  { id: 3, name: 'Llama-2', role: 'seer', isAlive: false, avatar: '/api/placeholder/40/40' },
  { id: 4, name: 'Anthropic-2', role: 'dire_wolf', isAlive: true, avatar: '/api/placeholder/40/40' },
  { id: 5, name: 'Gemini', role: 'villager', isAlive: true, avatar: '/api/placeholder/40/40' },
  { id: 6, name: 'PaLM', role: 'villager', isAlive: false, avatar: '/api/placeholder/40/40' },
];

// Message templates for simulation
const MESSAGE_TEMPLATES = {
  day: [
    "I think {player} has been acting suspicious...",
    "We should vote for {player} today.",
    "I can confirm that I'm a villager!",
    "Does anyone have any information to share?",
    "I saw something strange last night...",
    "I trust {player}, they've been helpful.",
    "We need to work together to find the wolves!",
    "I've been watching {player} carefully...",
    "Let's think about who hasn't spoken much.",
    "Can anyone verify {player}'s claim?",
  ],
  night: [
    "*moves silently through the village*",
    "*investigates carefully*",
    "*makes a difficult choice*",
    "*watches from the shadows*",
    "*performs their night action*",
    "*considers their options*",
    "*waits patiently*",
    "*makes a strategic decision*",
  ],
  system: [
    "🌙 Night falls on the village...",
    "☀️ Dawn breaks. A new day begins.",
    "The village must now vote...",
    "A howl echoes through the night...",
    "The village falls into an uneasy sleep...",
    "Tension rises as the sun sets...",
  ]
};

const getRoleColor = (role) => {
  switch (role) {
    case 'werewolf':
      return 'bg-red-600';
    case 'dire_wolf':
      return 'bg-red-800';
    case 'seer':
      return 'bg-purple-600';
    case 'villager':
      return 'bg-blue-600';
    default:
      return 'bg-gray-600';
  }
};

const getRandomMessage = (type, players) => {
  const templates = MESSAGE_TEMPLATES[type];
  let message = templates[Math.floor(Math.random() * templates.length)];
  
  // Replace {player} placeholder with random player name
  if (message.includes("{player}")) {
    const randomPlayer = players[Math.floor(Math.random() * players.length)];
    message = message.replace("{player}", randomPlayer.name);
  }
  
  return message;
};

const getTimeString = () => {
  const now = new Date();
  return `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
};

const WerewolfGame = () => {
  const [isNight, setIsNight] = useState(false);
  const [messages, setMessages] = useState([]);
  const [messageCount, setMessageCount] = useState(0);
  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const interval = setInterval(() => {
      // Toggle day/night every 5 messages
      if (messageCount > 0 && messageCount % 5 === 0) {
        setIsNight(prev => !prev);
      }

      // Generate a new message
      const messageType = Math.random() < 0.2 ? 'system' : (isNight ? 'night' : 'day');
      const newMessage = {
        id: messageCount + 1,
        phase: messageType,
        timestamp: getTimeString(),
      };

      if (messageType === 'system') {
        newMessage.message = getRandomMessage('system', MOCK_PLAYERS);
      } else {
        const randomPlayer = MOCK_PLAYERS.filter(p => p.isAlive)[
          Math.floor(Math.random() * MOCK_PLAYERS.filter(p => p.isAlive).length)
        ];
        newMessage.player = randomPlayer;
        newMessage.message = getRandomMessage(messageType, MOCK_PLAYERS);
      }

      setMessages(prev => [...prev, newMessage]);
      setMessageCount(prev => prev + 1);
    }, 4000);

    return () => clearInterval(interval);
  }, [isNight, messageCount]);

  return (
    <div className={`w-full min-h-screen p-4 transition-colors duration-500 flex flex-col ${isNight ? 'bg-gray-900' : 'bg-gray-100'}`}>
      <div className="max-w-4xl w-full mx-auto flex flex-col flex-grow">
        {/* Header with game controls */}
        <div className="flex justify-between items-center mb-4">
          <h1 className={`text-2xl font-bold ${isNight ? 'text-white' : 'text-gray-900'}`}>
            Werewolf Game
          </h1>
          <div className="flex items-center space-x-4">
            <span className={`${isNight ? 'text-white' : 'text-gray-900'}`}>
              {isNight ? 'Night Phase' : 'Day Phase'}
            </span>
            <button
              onClick={() => setIsNight(!isNight)}
              className="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700"
            >
              {isNight ? <Sun className="text-white" /> : <Moon className="text-gray-900" />}
            </button>
          </div>
        </div>

        {/* Scoreboard */}
        <div className={`mb-4 p-4 rounded-lg ${isNight ? 'bg-gray-800' : 'bg-white'} shadow-lg flex-shrink-0`}>
          <h2 className={`text-lg font-semibold mb-2 ${isNight ? 'text-white' : 'text-gray-900'}`}>
            Players
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {MOCK_PLAYERS.map((player) => (
              <div
                key={player.id}
                className={`flex items-center space-x-2 p-2 rounded ${
                  isNight ? 'bg-gray-700' : 'bg-gray-100'
                } ${!player.isAlive && 'opacity-50'}`}
              >
                <img
                  src={player.avatar}
                  alt={`${player.name}'s avatar`}
                  className="w-8 h-8 rounded-full"
                />
                <div>
                  <div className={`font-medium ${isNight ? 'text-white' : 'text-gray-900'}`}>
                    {player.name}
                  </div>
                  <div className="flex items-center space-x-2">
                    <span className={`w-2 h-2 rounded-full ${getRoleColor(player.role)}`} />
                    <span className={`text-sm ${isNight ? 'text-gray-300' : 'text-gray-600'}`}>
                      {!player.isAlive && '💀 '}
                      {player.role.charAt(0).toUpperCase() + player.role.slice(1).replace('_', ' ')}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Chat History */}
        <div className={`p-4 rounded-lg ${isNight ? 'bg-gray-800' : 'bg-white'} shadow-lg flex-grow`}>
          <div className="space-y-4 overflow-y-auto pr-4" style={{ maxHeight: 'calc(100vh - 300px)' }}>
            {messages.map((message) => {
              if (message.phase === 'system') {
                return (
                  <div
                    key={message.id}
                    className={`text-center italic ${
                      isNight ? 'text-gray-400' : 'text-gray-600'
                    }`}
                  >
                    {message.message}
                  </div>
                );
              }

              return (
                <div key={message.id} className="flex space-x-3">
                  {message.player && (
                    <img
                      src={message.player.avatar}
                      alt={`${message.player.name}'s avatar`}
                      className="w-8 h-8 rounded-full"
                    />
                  )}
                  <div className="flex-1">
                    <div className="flex items-center space-x-2">
                      <span className={`font-medium ${isNight ? 'text-white' : 'text-gray-900'}`}>
                        {message.player?.name}
                      </span>
                      <span className={`text-sm ${isNight ? 'text-gray-400' : 'text-gray-600'}`}>
                        {message.timestamp}
                      </span>
                      {message.phase === 'night' && <Moon className="w-4 h-4 text-gray-400" />}
                    </div>
                    <p className={`mt-1 ${isNight ? 'text-gray-300' : 'text-gray-700'}`}>
                      {message.message}
                    </p>
                  </div>
                </div>
              );
            })}
            <div ref={chatEndRef} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default WerewolfGame;