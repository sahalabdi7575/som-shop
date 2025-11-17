// static/js/main.js

// Main JavaScript for SomaliShop E-commerce

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    initializeMobileMenu();
    initializeCartFunctionality();
    initializeSearchFunctionality();
    initializeFormValidations();
    initializeImageLazyLoading();
    initializeSmoothScrolling();
    initializeToastNotifications();
}

// Mobile Menu Functionality
function initializeMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const adminMobileMenuBtn = document.getElementById('adminMobileMenuBtn');
    const adminMobileMenu = document.getElementById('adminMobileMenu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('slide-in');
        });
    }

    if (adminMobileMenuBtn && adminMobileMenu) {
        adminMobileMenuBtn.addEventListener('click', function() {
            adminMobileMenu.classList.toggle('hidden');
            adminMobileMenu.classList.toggle('slide-in');
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (mobileMenu && !mobileMenu.contains(event.target) && mobileMenuBtn && !mobileMenuBtn.contains(event.target)) {
            mobileMenu.classList.add('hidden');
        }
        if (adminMobileMenu && !adminMobileMenu.contains(event.target) && adminMobileMenuBtn && !adminMobileMenuBtn.contains(event.target)) {
            adminMobileMenu.classList.add('hidden');
        }
    });
}

// Cart Functionality
function initializeCartFunctionality() {
    // Cart count update
    updateCartCountDisplay();
    
    // Cart item quantity controls
    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const action = this.dataset.action;
            updateCartQuantity(productId, action);
        });
    });
}

function updateCartCountDisplay() {
    const cart = getCartFromStorage();
    const cartCountElements = document.querySelectorAll('.cart-count');
    
    cartCountElements.forEach(element => {
        if (cart.length > 0) {
            element.textContent = cart.length;
            element.classList.remove('hidden');
        } else {
            element.classList.add('hidden');
        }
    });
}

function getCartFromStorage() {
    try {
        return JSON.parse(localStorage.getItem('somaliShopCart')) || [];
    } catch (error) {
        console.error('Error reading cart from storage:', error);
        return [];
    }
}

function saveCartToStorage(cart) {
    try {
        localStorage.setItem('somaliShopCart', JSON.stringify(cart));
    } catch (error) {
        console.error('Error saving cart to storage:', error);
    }
}

function updateCartQuantity(productId, action) {
    let cart = getCartFromStorage();
    const itemIndex = cart.findIndex(item => item.product_id === productId);
    
    if (itemIndex !== -1) {
        if (action === 'increase') {
            cart[itemIndex].quantity += 1;
        } else if (action === 'decrease') {
            cart[itemIndex].quantity -= 1;
            if (cart[itemIndex].quantity <= 0) {
                cart.splice(itemIndex, 1);
            }
        }
        
        saveCartToStorage(cart);
        updateCartCountDisplay();
        showToast('Cart updated successfully', 'success');
        
        // Update cart page if we're on it
        if (window.location.pathname.includes('cart')) {
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    }
}

// Search Functionality
function initializeSearchFunctionality() {
    const searchInput = document.querySelector('input[name="search"]');
    const searchForm = document.querySelector('form[method="GET"]');
    
    if (searchInput && searchForm) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                if (this.value.length >= 2 || this.value.length === 0) {
                    searchForm.submit();
                }
            }, 500);
        });
    }
}

// Form Validations
function initializeFormValidations() {
    // Email validation
    const emailInputs = document.querySelectorAll('input[type="email"]');
    emailInputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateEmail(this);
        });
    });
    
    // Phone number validation
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('blur', function() {
            validatePhoneNumber(this);
        });
    });
    
    // Password strength
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(input => {
        input.addEventListener('input', function() {
            checkPasswordStrength(this);
        });
    });
}

function validateEmail(input) {
    const email = input.value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (email && !emailRegex.test(email)) {
        showInputError(input, 'Please enter a valid email address');
        return false;
    } else {
        clearInputError(input);
        return true;
    }
}

function validatePhoneNumber(input) {
    const phone = input.value;
    // Basic international phone validation
    const phoneRegex = /^\+?[\d\s\-\(\)]{10,}$/;
    
    if (phone && !phoneRegex.test(phone)) {
        showInputError(input, 'Please enter a valid phone number');
        return false;
    } else {
        clearInputError(input);
        return true;
    }
}

function checkPasswordStrength(input) {
    const password = input.value;
    const strengthIndicator = input.parentNode.querySelector('.password-strength');
    
    if (!strengthIndicator) return;
    
    let strength = 0;
    let feedback = '';
    
    if (password.length >= 8) strength++;
    if (password.match(/[a-z]/) && password.match(/[A-Z]/)) strength++;
    if (password.match(/\d/)) strength++;
    if (password.match(/[^a-zA-Z\d]/)) strength++;
    
    switch (strength) {
        case 0:
        case 1:
            feedback = 'Weak';
            strengthIndicator.className = 'password-strength text-red-600 text-sm';
            break;
        case 2:
        case 3:
            feedback = 'Medium';
            strengthIndicator.className = 'password-strength text-yellow-600 text-sm';
            break;
        case 4:
            feedback = 'Strong';
            strengthIndicator.className = 'password-strength text-green-600 text-sm';
            break;
    }
    
    strengthIndicator.textContent = feedback;
}

function showInputError(input, message) {
    clearInputError(input);
    
    input.classList.add('border-red-500');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'text-red-500 text-sm mt-1';
    errorDiv.textContent = message;
    
    input.parentNode.appendChild(errorDiv);
}

function clearInputError(input) {
    input.classList.remove('border-red-500');
    const existingError = input.parentNode.querySelector('.text-red-500');
    if (existingError) {
        existingError.remove();
    }
}

// Image Lazy Loading
function initializeImageLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    } else {
        // Fallback for older browsers
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Smooth Scrolling
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Toast Notifications
function initializeToastNotifications() {
    // Toast container will be created on first use
}

function showToast(message, type = 'info', duration = 3000) {
    let toastContainer = document.getElementById('toast-container');
    
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'fixed top-4 right-4 z-50 space-y-2';
        document.body.appendChild(toastContainer);
    }
    
    const toast = document.createElement('div');
    const typeClasses = {
        success: 'bg-green-500 text-white',
        error: 'bg-red-500 text-white',
        warning: 'bg-yellow-500 text-white',
        info: 'bg-blue-500 text-white'
    };
    
    toast.className = `p-4 rounded-lg shadow-lg transform transition-transform duration-300 ${typeClasses[type] || typeClasses.info}`;
    toast.textContent = message;
    
    toastContainer.appendChild(toast);
    
    // Animate in
    setTimeout(() => {
        toast.classList.add('translate-x-0');
    }, 10);
    
    // Remove after duration
    setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-x-full');
        setTimeout(() => {
            toast.remove();
            // Remove container if empty
            if (toastContainer.children.length === 0) {
                toastContainer.remove();
            }
        }, 300);
    }, duration);
}

// API Helper Functions
async function apiCall(endpoint, options = {}) {
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'same-origin'
    };
    
    const config = { ...defaultOptions, ...options };
    
    try {
        const response = await fetch(endpoint, config);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.message || 'API request failed');
        }
        
        return data;
    } catch (error) {
        console.error('API call failed:', error);
        showToast(error.message || 'Request failed', 'error');
        throw error;
    }
}

// Product Search with Debounce
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Currency Formatter
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Local Storage Helpers
class StorageHelper {
    static set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (error) {
            console.error('Storage set failed:', error);
            return false;
        }
    }
    
    static get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (error) {
            console.error('Storage get failed:', error);
            return defaultValue;
        }
    }
    
    static remove(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (error) {
            console.error('Storage remove failed:', error);
            return false;
        }
    }
}

// Export functions for global use
window.showToast = showToast;
window.formatCurrency = formatCurrency;
window.apiCall = apiCall;
window.StorageHelper = StorageHelper;

// Error boundary for the entire app
window.addEventListener('error', function(event) {
    console.error('Global error caught:', event.error);
    showToast('Something went wrong. Please try again.', 'error');
});

// Online/Offline detection
window.addEventListener('online', function() {
    showToast('Connection restored', 'success');
});

window.addEventListener('offline', function() {
    showToast('You are offline. Some features may not work.', 'warning');
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(() => {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            console.log(`Page loaded in ${loadTime}ms`);
            
            if (loadTime > 3000) {
                console.warn('Page load time is slow:', loadTime);
            }
        }, 0);
    });
}