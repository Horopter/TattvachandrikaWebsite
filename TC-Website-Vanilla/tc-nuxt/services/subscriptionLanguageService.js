import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscription-languages/'; // Adjust the URL to your API endpoint

const getSubscriptionLanguages = () => {
  return axios.get(apiUrl);
};

const getSubscriptionLanguageById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createSubscriptionLanguage = (subscriptionLanguage) => {
  return axios.post(apiUrl, subscriptionLanguage);
};

const updateSubscriptionLanguage = (id, subscriptionLanguage) => {
  return axios.put(`${apiUrl}${id}/`, subscriptionLanguage);
};

const deleteSubscriptionLanguage = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriptionLanguages,
  getSubscriptionLanguageById,
  createSubscriptionLanguage,
  updateSubscriptionLanguage,
  deleteSubscriptionLanguage
};
