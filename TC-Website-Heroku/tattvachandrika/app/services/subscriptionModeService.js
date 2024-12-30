import axios from "axios";

const apiUrl = "https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-modes/"; // Adjust the URL to your API endpoint

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

// Function to get subscription modes (GET)
const getSubscriptionModes = (searchText = "") => {
  const token = getToken();  // Assume getToken() retrieves the token
  console.log("name: ", searchText);

  // Sending token in the Authorization header
  return axiosInstance.get("", {
    params: {
      name: searchText, // Send searchText as a query param
    },
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a subscription mode by its ID (GET)
const getSubscriptionModeById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new subscription mode (POST)
const createSubscriptionMode = (subscriptionMode) => {
  console.log("newMode: ", subscriptionMode);
  const token = getToken();
  return axiosInstance.post("", 
    subscriptionMode,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a subscription mode by ID (PUT)
const updateSubscriptionMode = (id, subscriptionMode) => {
  const token = getToken();
  return axiosInstance.put(`${id}/`, 
    subscriptionMode,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a subscription mode by ID (DELETE)
const deleteSubscriptionMode = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
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
