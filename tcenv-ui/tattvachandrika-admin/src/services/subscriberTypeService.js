import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscriber-types/'; // Adjust the URL to your API endpoint

const getSubscriberTypes = () => {
  return axios.get(apiUrl);
};

const getSubscriberTypeById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createSubscriberType = (subscriberType) => {
  return axios.post(apiUrl, subscriberType);
};

const updateSubscriberType = (id, subscriberType) => {
  return axios.put(`${apiUrl}${id}/`, subscriberType);
};

const deleteSubscriberType = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

export default {
  getSubscriberTypes,
  getSubscriberTypeById,
  createSubscriberType,
  updateSubscriberType,
  deleteSubscriberType
};
