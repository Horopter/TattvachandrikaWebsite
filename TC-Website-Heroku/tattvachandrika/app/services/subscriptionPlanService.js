import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-plans/';
const languageApiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-languages/';
const modeApiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-modes/';

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

// Function to get all plans (GET)
const getPlans = () => {
  const token = getToken();
  return axiosInstance.get("", {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get a plan by its ID (GET)
const getPlanById = (id) => {
  const token = getToken();
  return axiosInstance.get(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to create a new plan (POST)
const createPlan = (plan) => {
  const token = getToken();
  return axiosInstance.post(
    "", 
    plan,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to update a plan by ID (PUT)
const updatePlan = (id, plan) => {
  const token = getToken();
  return axiosInstance.put(
    `${id}/`, 
    plan,
    {
      headers: {
        Authorization: `Bearer ${token}`,  // Pass token in the header
      },
    }
  );
};

// Function to delete a plan by ID (DELETE)
const deletePlan = (id) => {
  const token = getToken();
  return axiosInstance.delete(`${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get all subscription languages (GET)
const getLanguages = () => {
  const token = getToken();
  return axios.get(languageApiUrl, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

// Function to get all subscription modes (GET)
const getModes = () => {
  const token = getToken();
  return axios.get(modeApiUrl, {
    headers: {
      Authorization: `Bearer ${token}`,  // Pass token in the header
    },
  });
};

export default {
  getPlans,
  getPlanById,
  createPlan,
  updatePlan,
  deletePlan,
  getLanguages,
  getModes,
};
