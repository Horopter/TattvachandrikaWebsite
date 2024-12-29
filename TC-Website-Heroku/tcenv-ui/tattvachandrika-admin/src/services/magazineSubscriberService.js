import axios from 'axios';

const apiUrl = 'https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscribers/';

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
  return axios.get('https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-categories/');
};

const getTypes = () => {
  return axios.get('https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/subscriber-types/');
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
