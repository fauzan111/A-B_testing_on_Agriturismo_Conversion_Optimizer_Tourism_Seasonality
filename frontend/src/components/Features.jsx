import React from 'react';

const Features = ({ variant, t, selectedFeature, onSelect }) => {
    const content = variant === 'A' ? t.variantA : t.variantB;

    const getCardStyle = (featureName) => ({
        border: selectedFeature === featureName ? '2px solid var(--color-olive)' : '2px solid transparent',
        transform: selectedFeature === featureName ? 'scale(1.05)' : 'scale(1)',
        cursor: 'pointer',
        transition: 'all 0.3s ease'
    });

    return (
        <section className="container features">
            <div
                className="feature-card"
                style={getCardStyle(content.feature1)}
                onClick={() => onSelect(content.feature1)}
            >
                <div className="feature-icon">
                    {variant === 'A' ? '🏊' : '🍇'}
                </div>
                <h3>{content.feature1}</h3>
                <p>{content.feature1Desc}</p>
            </div>
            <div
                className="feature-card"
                style={getCardStyle(content.feature2)}
                onClick={() => onSelect(content.feature2)}
            >
                <div className="feature-icon">
                    {variant === 'A' ? '💆' : '🍝'}
                </div>
                <h3>{content.feature2}</h3>
                <p>{content.feature2Desc}</p>
            </div>
            <div
                className="feature-card"
                style={getCardStyle(content.feature3)}
                onClick={() => onSelect(content.feature3)}
            >
                <div className="feature-icon">
                    {variant === 'A' ? '🏨' : '🌳'}
                </div>
                <h3>{content.feature3}</h3>
                <p>{content.feature3Desc}</p>
            </div>
        </section>
    );
};

export default Features;
