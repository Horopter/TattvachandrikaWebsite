import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-categories/'; // Adjust the URL to your API endpoint

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

// Function to get subscriber categories (GET)
const getSubscriberCategories = () => {
  const token = getToken();
  
  // Sending token in the Authorization header
  return axiosInstance.get("", {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a subscriber category by its ID (GET)
const getSubscriberCategoryById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new subscriber category (POST)
const createSubscriberCategory = (subscriberCategory) => {
  const token = getToken();
  return axiosInstance.post(
    "", 
    subscriberCategory,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a subscriber category by ID (PUT)
const updateSubscriberCategory = (id, subscriberCategory) => {
  const token = getToken();
  return axiosInstance.put(
    `${id}/`, 
    subscriberCategory,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a subscriber category by ID (DELETE)
const deleteSubscriberCategory = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

export default {
  getSubscriberCategories,
  getSubscriberCategoryById,
  createSubscriberCategory,
  updateSubscriberCategory,
  deleteSubscriberCategory,
};
