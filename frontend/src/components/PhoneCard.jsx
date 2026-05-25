import React from 'react';

const PhoneCard = ({ phone }) => {
  // Score could be out of 1 or very small depending on the matrix
  // Just show it as a percentage or score points
  const matchPercentage = Math.round((phone.Score || 0) * 100);
  
  return (
    <div className="bg-slate-800 rounded-xl overflow-hidden shadow-lg hover:shadow-cyan-500/20 hover:-translate-y-1 transition-all duration-300 border border-slate-700 p-6 flex flex-col h-full relative">
      <div className="absolute top-0 right-0 bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-bold text-xs py-1 px-3 rounded-bl-xl">
        {matchPercentage > 0 ? `Match ${matchPercentage}%` : 'Recommended'}
      </div>
      
      <div className="flex items-center justify-between mb-4 mt-2">
        <h3 className="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400">
          {phone.Brand} {phone.Model}
        </h3>
      </div>
      
      <div className="space-y-3 flex-grow text-sm text-slate-300">
        <div className="flex justify-between items-center bg-slate-900/50 p-2 rounded-lg">
          <span className="font-semibold text-slate-400">Price</span>
          <span className="text-green-400 font-bold">₹{phone.Prices}</span>
        </div>
        
        <div className="flex justify-between items-center bg-slate-900/50 p-2 rounded-lg">
          <span className="font-semibold text-slate-400">Rating</span>
          <span className="text-yellow-400 font-bold flex items-center gap-1">
            {phone.Ratings} ★
          </span>
        </div>
        
        <div className="grid grid-cols-2 gap-2 mt-4 text-xs">
          <div className="bg-slate-800 p-2 rounded border border-slate-700 flex flex-col items-center text-center justify-center">
            <span className="text-slate-500 mb-1">RAM</span>
            <span className="font-semibold">{phone.RAM} GB</span>
          </div>
          <div className="bg-slate-800 p-2 rounded border border-slate-700 flex flex-col items-center text-center justify-center">
            <span className="text-slate-500 mb-1">Battery</span>
            <span className="font-semibold">{phone.Battery} mAh</span>
          </div>
          <div className="bg-slate-800 p-2 rounded border border-slate-700 flex flex-col items-center text-center justify-center col-span-2">
            <span className="text-slate-500 mb-1">Camera</span>
            <span className="font-semibold truncate w-full px-2" title={phone.Camera}>{phone.Camera} MP</span>
          </div>
          <div className="bg-slate-800 p-2 rounded border border-slate-700 flex flex-col items-center text-center justify-center col-span-2">
            <span className="text-slate-500 mb-1">Processor</span>
            <span className="font-semibold truncate w-full px-2" title={phone.Processor}>{phone.Processor}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PhoneCard;
