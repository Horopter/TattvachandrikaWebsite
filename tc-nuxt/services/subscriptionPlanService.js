import axios from 'axios';

const apiUrl = 'http://localhost:8000/api/subscription-plans/';
const languageApiUrl = 'http://localhost:8000/api/subscription-languages/';
const modeApiUrl = 'http://localhost:8000/api/subscription-modes/';

const getPlans = () => {
  return axios.get(apiUrl);
};

const getPlanById = (id) => {
  return axios.get(`${apiUrl}${id}/`);
};

const createPlan = (plan) => {
  return axios.post(apiUrl, plan);
};

const updatePlan = (id, plan) => {
  return axios.put(`${apiUrl}${id}/`, plan);
};

const deletePlan = (id) => {
  return axios.delete(`${apiUrl}${id}/`);
};

const getLanguages = () => {
  return axios.get(languageApiUrl);
};

const getModes = () => {
  return axios.get(modeApiUrl);
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
