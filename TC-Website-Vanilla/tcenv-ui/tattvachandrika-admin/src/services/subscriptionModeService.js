import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscription-modes/'; // Adjust the URL to your API endpoint

const getSubscriptionModes = (url = apiUrl, searchText = '') => {
  return axios.get(url, {
    params: {
      name: searchText
    }
  });
};

const getSubscriptionModeById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createSubscriptionMode = (subscriptionMode) => {
  return axios.post(apiUrl, subscriptionMode);
};

const updateSubscriptionMode = (id, subscriptionMode) => {
  return axios.put(`${apiUrl}${id}/`, subscriptionMode);
};

const deleteSubscriptionMode = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriptionModes,
  getSubscriptionModeById,
  createSubscriptionMode,
  updateSubscriptionMode,
  deleteSubscriptionMode
};
