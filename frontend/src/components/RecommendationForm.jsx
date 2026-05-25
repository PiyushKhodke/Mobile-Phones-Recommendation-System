import React, { useState } from 'react';

const RecommendationForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    brand: '',
    price: '',
    camera: '',
    battery: '',
    processor: '',
    ram: '',
    ratings: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const inputClasses = "w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-colors placeholder-slate-600";
  const labelClasses = "block text-sm font-medium text-slate-400 mb-1";

  return (
    <form onSubmit={handleSubmit} className="bg-slate-800/80 backdrop-blur-xl border border-slate-700 p-8 rounded-2xl shadow-2xl">
      <h2 className="text-2xl font-bold mb-6 text-white text-center">Find Your Perfect Phone</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label className={labelClasses}>Brand preference</label>
          <input type="text" name="brand" value={formData.brand} onChange={handleChange} placeholder="e.g. Samsung, Apple, Poco" className={inputClasses} />
        </div>
        
        <div>
          <label className={labelClasses}>Max Price (₹)</label>
          <input type="number" name="price" value={formData.price} onChange={handleChange} placeholder="e.g. 50000" className={inputClasses} />
        </div>
        
        <div>
          <label className={labelClasses}>Min RAM (GB)</label>
          <input type="number" name="ram" value={formData.ram} onChange={handleChange} placeholder="e.g. 8" className={inputClasses} />
        </div>
        
        <div>
          <label className={labelClasses}>Min Battery (mAh)</label>
          <input type="number" name="battery" value={formData.battery} onChange={handleChange} placeholder="e.g. 4500" className={inputClasses} />
        </div>
        
        <div>
          <label className={labelClasses}>Min Camera (MP)</label>
          <input type="number" name="camera" value={formData.camera} onChange={handleChange} placeholder="e.g. 48" className={inputClasses} />
        </div>
        
        <div>
          <label className={labelClasses}>Min Rating</label>
          <input type="number" step="0.1" max="5" name="ratings" value={formData.ratings} onChange={handleChange} placeholder="e.g. 4.0" className={inputClasses} />
        </div>
        
        <div className="md:col-span-2">
          <label className={labelClasses}>Processor (Optional)</label>
          <input type="text" name="processor" value={formData.processor} onChange={handleChange} placeholder="e.g. Snapdragon, Dimensity" className={inputClasses} />
        </div>
      </div>
      
      <div className="mt-8">
        <button 
          type="submit" 
          disabled={isLoading}
          className="w-full bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg shadow-cyan-500/30 transform transition hover:-translate-y-0.5 active:translate-y-0 focus:outline-none flex justify-center items-center disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
        >
          {isLoading ? (
            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          ) : null}
          {isLoading ? 'Searching...' : 'Get Recommendations'}
        </button>
      </div>
    </form>
  );
};

export default RecommendationForm;
