document.addEventListener('DOMContentLoaded', () => {
    const skinTypeSelect = document.getElementById('skin-type');
    const skinConcernSelect = document.getElementById('skin-concern');
    const form = document.getElementById('recommendation-form');
    const btnText = document.querySelector('#submit-btn span');
    const spinner = document.getElementById('btn-spinner');
    const submitBtn = document.getElementById('submit-btn');
    const resultsSection = document.getElementById('results-section');
    const productGrid = document.getElementById('product-grid');

    const API_BASE = '/api';

    // Fetch Options on load
    fetch(`${API_BASE}/options`)
        .then(res => res.json())
        .then(data => {
            populateSelect(skinTypeSelect, data.skin_types, "Select your skin type");
            populateSelect(skinConcernSelect, data.skin_concerns, "Select your primary concern");
        })
        .catch(err => {
            console.error("Failed to load options from backend", err);
            skinTypeSelect.innerHTML = `<option value="">Error loading options. Ensure backend is running.</option>`;
            skinConcernSelect.innerHTML = `<option value="">Error loading options.</option>`;
        });


    function populateSelect(selectEl, options, placeholder) {
        selectEl.innerHTML = `<option value="" disabled selected>${placeholder}</option>`;
        // Sort options alphabetically for better UX
        options.sort().forEach(opt => {
            const tag = document.createElement('option');
            tag.value = opt;
            // capitalize first letter
            tag.textContent = opt.charAt(0).toUpperCase() + opt.slice(1);
            selectEl.appendChild(tag);
        });
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const skinType = skinTypeSelect.value;
        const skinConcern = skinConcernSelect.value;
        if (!skinType || !skinConcern) return;

        // UI Loading State
        btnText.classList.add('hidden');
        spinner.classList.remove('hidden');
        submitBtn.disabled = true;

        try {
            const response = await fetch(`${API_BASE}/recommend`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    skin_type: skinType,
                    skin_concern: skinConcern
                })
            });

            if (!response.ok) throw new Error("API responded with an error");

            const data = await response.json();
            renderResults(data.recommendations);
        } catch (error) {
            console.error(error);
            alert("Error fetching recommendations. Please try again.");
        } finally {
            // Restore UI
            btnText.classList.remove('hidden');
            spinner.classList.add('hidden');
            submitBtn.disabled = false;
        }
    });

    function renderResults(products) {
        productGrid.innerHTML = ''; // clear 

        products.forEach((product, i) => {
            const card = document.createElement('div');
            card.className = 'glass-panel product-card';
            // Staggered animation
            card.style.opacity = '0';
            card.style.animation = `fadeInUp 0.6s ease ${i * 0.15 + 0.2}s forwards`;

            const priceStr = product.price === 'N/A' ? 'Price Unavailable' : `${product.price}`;
            
            card.innerHTML = `
                <div class="product-type">${product.product_type}</div>
                <h3 class="product-name">${product.product_name}</h3>
                <div class="product-price">${priceStr}</div>
                <a href="${product.product_url !== '#' ? product.product_url : '#'}" target="_blank" class="btn-outline">
                    ${product.product_url !== '#' ? 'View Details' : 'Not Available'}
                </a>
            `;
            productGrid.appendChild(card);
        });

        resultsSection.classList.remove('hidden');
        // small timeout to allow display:block to apply before animating opacity
        setTimeout(() => {
            resultsSection.classList.add('visible');
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 50);
    }
});
