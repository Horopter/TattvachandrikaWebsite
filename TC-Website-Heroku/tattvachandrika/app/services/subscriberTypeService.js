import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-types/'; // Adjust the URL to your API endpoint

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

// Function to get subscriber types (GET)
const getSubscriberTypes = () => {
  const token = getToken();
  
  // Sending token in the Authorization header
  return axiosInstance.get("", {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a subscriber type by its ID (GET)
const getSubscriberTypeById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new subscriber type (POST)
const createSubscriberType = (subscriberType) => {
  const token = getToken();
  return axiosInstance.post(
    "", 
    subscriberType,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a subscriber type by ID (PUT)
const updateSubscriberType = (id, subscriberType) => {
  const token = getToken();
  return axiosInstance.put(
    `${id}/`, 
    subscriberType,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a subscriber type by ID (DELETE)
const deleteSubscriberType = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

export default {
  getSubscriberTypes,
  getSubscriberTypeById,
  createSubscriberType,
  updateSubscriberType,
  deleteSubscriberType,
};
