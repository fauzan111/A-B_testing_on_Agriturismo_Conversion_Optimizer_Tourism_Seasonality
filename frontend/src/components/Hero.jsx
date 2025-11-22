import React from 'react';

const Hero = ({ variant, t }) => {
    // In a real app, we would import images. For now, we use placeholders or CSS backgrounds.
    // Variant A: Pool (Blue/Water theme)
    // Variant B: Vineyard (Green/Nature theme)

    const bgStyle = {
        backgroundColor: variant === 'A' ? '#87CEEB' : '#6B8E23', // SkyBlue vs OliveDrab fallback
        // We can use a gradient or url() here
        backgroundImage: variant === 'A'
            ? 'linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url("https://images.unsplash.com/photo-1572331165267-854da2b00cc3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")' // Pool
            : 'linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url("https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")' // Vineyard
    };

    const content = variant === 'A' ? t.variantA : t.variantB;

    return (
        <section className="hero" style={bgStyle}>
            <div className="container hero-content">
                <h1>{content.heroTitle}</h1>
                <p style={{ fontSize: '1.5rem', marginBottom: '20px' }}>{content.heroSubtitle}</p>
                <button className="cta-button" onClick={() => document.getElementById('booking').scrollIntoView({ behavior: 'smooth' })}>
                    {t.bookNow}
                </button>
            </div>
        </section>
    );
};

export default Hero;
