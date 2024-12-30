import axios from 'axios';

// API URLs
const API_URL = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscribers/';
const API_CATEGORIES_URL = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-categories/';
const API_TYPES_URL = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-types/';

// Function to get the stored token
const getToken = () => {
  if (import.meta.client) {
    return localStorage.getItem('token'); // Access localStorage only on the client
  }
  return null; // Return null if not on the client
};

// Axios instance with default headers
const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    Authorization: `Bearer ${getToken()}`, // Token in Authorization header
  },
});

// Function to get all magazine subscribers (GET)
const getMagazineSubscribers = () => {
  return axiosInstance.get('');
};

// Function to get a magazine subscriber by ID (GET)
const getMagazineSubscriberById = (id) => {
  return axiosInstance.get(`${id}/`);
};

// Function to create a new magazine subscriber (POST)
const createMagazineSubscriber = (subscriber) => {
  return axiosInstance.post('', subscriber);
};

// Function to update an existing magazine subscriber by ID (PUT)
const updateMagazineSubscriber = (id, subscriber) => {
  return axiosInstance.put(`${id}/`, subscriber);
};

// Function to soft delete a magazine subscriber (DELETE)
const softDeleteMagazineSubscriber = (id) => {
  return axiosInstance.delete(`${id}/`);
};

// Function to activate a magazine subscriber (POST)
const activateMagazineSubscriber = (id) => {
  return axiosInstance.post(`${id}/activate/`);
};

// Function to get all subscriber categories (GET)
const getCategories = () => {
  return axiosInstance.get(API_CATEGORIES_URL);
};

// Function to get all subscriber types (GET)
const getTypes = () => {
  return axiosInstance.get(API_TYPES_URL);
};

export default {
  getMagazineSubscribers,
  getMagazineSubscriberById,
  createMagazineSubscriber,
  updateMagazineSubscriber,
  softDeleteMagazineSubscriber,
  activateMagazineSubscriber,
  getCategories,
  getTypes,
};
