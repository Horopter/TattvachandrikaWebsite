import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/payment-modes/';

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

// Function to get all payment modes (GET)
const getPaymentModes = () => {
  const token = getToken();
  return axiosInstance.get("", {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a payment mode by its ID (GET)
const getPaymentModeById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new payment mode (POST)
const createPaymentMode = (paymentMode) => {
  const token = getToken();
  return axiosInstance.post(
    "", 
    paymentMode,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a payment mode by ID (PUT)
const updatePaymentMode = (id, paymentMode) => {
  const token = getToken();
  return axiosInstance.put(
    `${id}/`, 
    paymentMode,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a payment mode by ID (DELETE)
const deletePaymentMode = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

export default {
  getPaymentModes,
  getPaymentModeById,
  createPaymentMode,
  updatePaymentMode,
  deletePaymentMode,
};
