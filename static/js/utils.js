// static/js/utils.js

// Utility functions for SomaliShop E-commerce

// Date formatting
function formatDate(dateString) {
    const options = { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// String truncation
function truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substr(0, maxLength) + '...';
}

// URL parameter handling
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

function setUrlParameter(name, value) {
    const url = new URL(window.location);
    url.searchParams.set(name, value);
    window.history.pushState({}, '', url);
}

// Form data serialization
function serializeForm(form) {
    const formData = new FormData(form);
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    return data;
}

// Input sanitization
function sanitizeInput(input) {
    const div = document.createElement('div');
    div.textContent = input;
    return div.innerHTML;
}

// Price calculation
function calculateTotal(items) {
    return items.reduce((total, item) => {
        return total + (item.price * item.quantity);
    }, 0);
}

function calculateTax(subtotal, taxRate = 0.1) {
    return subtotal * taxRate;
}

function calculateGrandTotal(subtotal, tax = 0, shipping = 0) {
    return subtotal + tax + shipping;
}

// Stock management
function isInStock(product) {
    return product.stock > 0;
}

function getStockStatus(product) {
    if (product.stock === 0) return 'out-of-stock';
    if (product.stock <= 5) return 'low-stock';
    return 'in-stock';
}

// Image handling
function getProductImageUrl(imageUrl, fallbackUrl = '/static/images/placeholder.jpg') {
    return imageUrl && imageUrl !== '' ? imageUrl : fallbackUrl;
}

function preloadImage(url) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.onerror = reject;
        img.src = url;
    });
}

// Localization (for future multi-language support)
const translations = {
    en: {
        add_to_cart: 'Add to Cart',
        out_of_stock: 'Out of Stock',
        loading: 'Loading...'
    }
};

function t(key, lang = 'en') {
    return translations[lang]?.[key] || key;
}

// Validation helpers
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const phoneRegex = /^\+?[\d\s\-\(\)]{10,}$/;
    return phoneRegex.test(phone);
}

function isValidPassword(password) {
    return password.length >= 8;
}

// Cart helpers
function getCartItemCount() {
    const cart = StorageHelper.get('somaliShopCart', []);
    return cart.reduce((count, item) => count + item.quantity, 0);
}

function getCartTotal() {
    const cart = StorageHelper.get('somaliShopCart', []);
    return calculateTotal(cart);
}

// API response handlers
function handleApiResponse(response, successMessage = null) {
    if (response.success) {
        if (successMessage) {
            showToast(successMessage, 'success');
        }
        return response.data;
    } else {
        throw new Error(response.message || 'Request failed');
    }
}

// Export utility functions
window.utils = {
    formatDate,
    truncateText,
    getUrlParameter,
    setUrlParameter,
    serializeForm,
    sanitizeInput,
    calculateTotal,
    calculateTax,
    calculateGrandTotal,
    isInStock,
    getStockStatus,
    getProductImageUrl,
    preloadImage,
    t,
    isValidEmail,
    isValidPhone,
    isValidPassword,
    getCartItemCount,
    getCartTotal,
    handleApiResponse
};