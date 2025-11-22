import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { translations } from './i18n';
import Hero from './components/Hero';
import Features from './components/Features';
import BookingForm from './components/BookingForm';
import './index.css';

function App() {
  const [variant, setVariant] = useState(null);
  const [userId, setUserId] = useState(null);
  const [lang, setLang] = useState('it'); // Default to Italian
  const [selectedFeature, setSelectedFeature] = useState(null);
  const t = translations[lang];

  useEffect(() => {
    // Fetch variant from backend
    const fetchVariant = async () => {
      try {
        // Check if user_id is already in localStorage to persist variant
        let storedUserId = localStorage.getItem('user_id');
        const response = await axios.get(`http://localhost:8000/api/experiment/variant${storedUserId ? `?user_id=${storedUserId}` : ''}`);

        setVariant(response.data.variant);
        setUserId(response.data.user_id);

        if (!storedUserId) {
          localStorage.setItem('user_id', response.data.user_id);
        }
      } catch (error) {
        console.error("Error fetching variant:", error);
        // Fallback to A if backend fails
        setVariant('A');
      }
    };

    fetchVariant();
  }, []);

  if (!variant) return <div>Loading...</div>;

  return (
    <div className="app">
      <header className="container">
        <div className="logo">{t.title}</div>
        <div className="lang-switch">
          <button onClick={() => setLang('it')} className={lang === 'it' ? 'active' : ''}>IT</button>
          <button onClick={() => setLang('en')} className={lang === 'en' ? 'active' : ''}>EN</button>
        </div>
      </header>

      <main>
        <Hero variant={variant} t={t} />
        <Features variant={variant} t={t} selectedFeature={selectedFeature} onSelect={setSelectedFeature} />
        <BookingForm userId={userId} variant={variant} t={t} selectedFeature={selectedFeature} />
      </main>

      <footer style={{ textAlign: 'center', padding: '20px', color: '#666' }}>
        &copy; 2024 Agriturismo Bella Vita. Variant: {variant}
      </footer>
    </div>
  );
}

export default App;
