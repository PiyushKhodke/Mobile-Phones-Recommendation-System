import React, { useState } from 'react';
import axios from 'axios';
import RecommendationForm from './components/RecommendationForm';
import PhoneCard from './components/PhoneCard';

function App() {
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState('');

  const fetchRecommendations = async (formData) => {
    setIsLoading(true);
    setMessage('');
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/recommend', formData);
      if (response.data.recommendations) {
        setRecommendations(response.data.recommendations);
      }
      if (response.data.message) {
        setMessage(response.data.message);
      }
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      setMessage('An error occurred while fetching recommendations. Make sure the backend is running.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 font-sans selection:bg-cyan-500/30">
      <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-[0.03] pointer-events-none"></div>
      
      <main className="container mx-auto px-4 py-12 relative z-10 max-w-6xl">
        <div className="text-center mb-16">
          <h1 className="text-5xl md:text-6xl font-extrabold mb-6 tracking-tight">
            Mobile <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">Recommendation</span> System
          </h1>
          <p className="text-xl text-slate-400 max-w-2xl mx-auto">
            Discover the perfect smartphone tailored exactly to your needs, budget, and preferences.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          <div className="lg:col-span-5 xl:col-span-4">
            <div className="sticky top-8">
              <RecommendationForm onSubmit={fetchRecommendations} isLoading={isLoading} />
            </div>
          </div>
          
          <div className="lg:col-span-7 xl:col-span-8">
            {message && recommendations.length === 0 && (
              <div className="bg-blue-500/10 border border-blue-500/50 text-blue-400 px-6 py-4 rounded-xl text-center backdrop-blur-sm">
                {message}
              </div>
            )}
            
            {message && recommendations.length > 0 && (
              <h2 className="text-2xl font-bold mb-6 flex items-center gap-2">
                <span className="w-2 h-8 bg-cyan-500 rounded-full inline-block"></span>
                Top Recommendations
              </h2>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {recommendations.map((phone, index) => (
                <PhoneCard key={index} phone={phone} index={index} />
              ))}
            </div>
            
            {!isLoading && recommendations.length === 0 && !message && (
              <div className="h-full flex flex-col items-center justify-center text-center p-12 border border-dashed border-slate-700 rounded-2xl bg-slate-800/30">
                <svg className="w-16 h-16 text-slate-600 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                <h3 className="text-xl font-medium text-slate-400 mb-2">Ready to find your match</h3>
                <p className="text-slate-500">Fill out the preferences form to discover the best mobile devices for you.</p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
