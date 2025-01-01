import axios from "axios";

const apiUrl = "http://localhost:8000/api/subscription-modes/"; // Adjust the URL to your API endpoint

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

const getSubscriptionModes = (searchText = "") => {
  const token = getToken();
  return axiosInstance.get("", {
    params: {
      name: searchText,
      token: token,
    },
  });
};

const getSubscriptionModeById = (id) => {
  return axiosInstance.get(`${id}/`, {
    params: {
      token: token,
    },
  });
};

const createSubscriptionMode = (subscriptionMode) => {
  return axiosInstance.post("", {
    params: {
      token: token,
      subscriptionMode: subscriptionMode
    },
  });
};

const updateSubscriptionMode = (id, subscriptionMode) => {
  return axiosInstance.put(`${id}/`, {
    params: {
      token: token,
      subscriptionMode: subscriptionMode
    },
  });
};

const deleteSubscriptionMode = (id) => {
  return axiosInstance.delete(`${id}/`, {
    params: {
      token: token,
    },
  });
};

export default {
  getSubscriptionModes,
  getSubscriptionModeById,
  createSubscriptionMode,
  updateSubscriptionMode,
  deleteSubscriptionMode,
};
