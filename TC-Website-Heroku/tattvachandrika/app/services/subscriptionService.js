import axios from 'axios';

// API URLs
const API_URL = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriptions/';
const API_PAYMENT_MODES_URL = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/payment-modes/';

// Function to get the stored token
const getToken = () => {
  if (import.meta.client) {
    return localStorage.getItem('token'); // Access localStorage only on the client
  }
  return null; // Return null if not on the client
};

// Create Axios instance with default headers (Authorization)
const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    Authorization: `Bearer ${getToken()}`, // Token in Authorization header
  },
});

// Function to get subscriptions (GET)
const getSubscriptions = () => {
  return axiosInstance.get('');
};

// Function to get subscription by ID (GET)
const getSubscriptionById = (id) => {
  return axiosInstance.get(`${id}/`);
};

// Function to create a new subscription (POST)
const createSubscription = (subscription) => {
  return axiosInstance.post('', subscription);
};

// Function to update an existing subscription by ID (PUT)
const updateSubscription = (id, subscription) => {
  return axiosInstance.put(`${id}/`, subscription);
};

// Function to get payment modes (GET)
const getPaymentModes = () => {
  return axiosInstance.get(API_PAYMENT_MODES_URL);
};

// Function to get subscriptions by subscriber (GET)
const getSubscriptionsBySubscriber = (subscriberId) => {
  return axiosInstance.get(`by_subscriber/${subscriberId}/`);
};

export default {
  getSubscriptions,
  getSubscriptionById,
  createSubscription,
  updateSubscription,
  getPaymentModes,
  getSubscriptionsBySubscriber,
};
