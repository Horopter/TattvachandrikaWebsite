import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-languages/'; // Adjust the URL to your API endpoint

// Function to get the stored token
const getToken = () => {
  if (import.meta.client) {
    return localStorage.getItem('token'); // Access localStorage only on the client
  }
  return null; // Return null if not on the client
};

// Axios instance with default headers
const axiosInstance = axios.create({
  baseURL: apiUrl,
});

// Function to get subscription languages (GET)
const getSubscriptionLanguages = () => {
  const token = getToken();
  
  // Sending token in the Authorization header
  return axiosInstance.get("", {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a subscription language by its ID (GET)
const getSubscriptionLanguageById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new subscription language (POST)
const createSubscriptionLanguage = (subscriptionLanguage) => {
  const token = getToken();
  return axiosInstance.post(
    "", 
    subscriptionLanguage,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a subscription language by ID (PUT)
const updateSubscriptionLanguage = (id, subscriptionLanguage) => {
  const token = getToken();
  return axiosInstance.put(
    `${id}/`, 
    subscriptionLanguage,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a subscription language by ID (DELETE)
const deleteSubscriptionLanguage = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

export default {
  getSubscriptionLanguages,
  getSubscriptionLanguageById,
  createSubscriptionLanguage,
  updateSubscriptionLanguage,
  deleteSubscriptionLanguage,
};
