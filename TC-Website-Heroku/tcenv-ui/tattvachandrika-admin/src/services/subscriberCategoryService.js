import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-categories/'; // Adjust the URL to your API endpoint

const getSubscriberCategories = () => {
  return axios.get(apiUrl);
};

const getSubscriberCategoryById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createSubscriberCategory = (subscriberCategory) => {
  return axios.post(apiUrl, subscriberCategory);
};

const updateSubscriberCategory = (id, subscriberCategory) => {
  return axios.put(`${apiUrl}${id}/`, subscriberCategory);
};

const deleteSubscriberCategory = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriberCategories,
  getSubscriberCategoryById,
  createSubscriberCategory,
  updateSubscriberCategory,
  deleteSubscriberCategory
};
