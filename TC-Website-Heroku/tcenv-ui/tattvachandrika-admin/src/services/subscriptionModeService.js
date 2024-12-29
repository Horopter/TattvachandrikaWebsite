import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscription-modes/'; // Adjust the URL to your API endpoint

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
