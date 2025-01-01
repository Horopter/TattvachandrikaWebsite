import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscribers/';

const getMagazineSubscribers = () => {
  return axios.get(apiUrl);
};

const getMagazineSubscriberById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createMagazineSubscriber = (subscriber) => {
  return axios.post(apiUrl, subscriber);
};

const updateMagazineSubscriber = (id, subscriber) => {
  return axios.put(`${apiUrl}${id}/`, subscriber);
};

const softDeleteMagazineSubscriber = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

const activateMagazineSubscriber = (id) => {
  return axios.post(`${apiUrl}${id}/activate/`);
};

const getCategories = () => {
  return axios.get('http://localhost:8000/api/subscriber-categories/');
};

const getTypes = () => {
  return axios.get('http://localhost:8000/api/subscriber-types/');
};

export default {
  getMagazineSubscribers,
  getMagazineSubscriberById,
  createMagazineSubscriber,
  updateMagazineSubscriber,
  softDeleteMagazineSubscriber,
  activateMagazineSubscriber,
  getCategories,
  getTypes
};
