import React, { useState } from 'react';
import axios from 'axios';

const BookingForm = ({ userId, variant, t, selectedFeature }) => {
    const [email, setEmail] = useState('');
    const [name, setName] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const validateEmail = (email) => {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        if (!selectedFeature) {
            setError(variant === 'A' ? 'Please select a package above (Pool, Spa, or Suite).' : 'Please select an experience above (Vineyard, Food, or Nature).');
            return;
        }

        if (!validateEmail(email)) {
            setError('Please enter a valid email address.');
            return;
        }

        setLoading(true);
        try {
            await axios.post('http://localhost:8000/api/book', {
                user_id: userId,
                variant: variant,
                region: 'Unknown',
                selected_feature: selectedFeature
            });
            setSubmitted(true);
        } catch (error) {
            console.error("Booking failed:", error);
            alert("Booking failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <section id="booking" className="booking-section">
            <div className="container">
                <h2>{t.bookNow}</h2>
                {selectedFeature && <p style={{ color: 'var(--color-olive)', fontWeight: 'bold' }}>Selected: {selectedFeature}</p>}
                {!submitted ? (
                    <form className="booking-form" onSubmit={handleSubmit}>
                        {error && <div style={{ color: 'red', marginBottom: '10px' }}>{error}</div>}
                        <input
                            type="text"
                            placeholder={t.namePlaceholder}
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                        />
                        <input
                            type="email"
                            placeholder={t.emailPlaceholder}
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                        <button type="submit" className="cta-button" disabled={loading}>
                            {loading ? '...' : t.submit}
                        </button>
                    </form>
                ) : (
                    <div className="success-message">
                        <h3>{t.success}</h3>
                        <p>We look forward to seeing you for your {selectedFeature} experience!</p>
                    </div>
                )}
            </div>
        </section>
    );
};

export default BookingForm;
