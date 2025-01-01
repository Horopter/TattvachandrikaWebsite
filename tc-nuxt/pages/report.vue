<template>
    <div class="container mx-auto p-6">
      <h1 class="title">Generate Report</h1>
      <nav aria-label="breadcrumb" class="mb-6">
        <ol class="flex space-x-2 text-gray-700">
          <li>
            <router-link to="/HomePage" class="text-blue-600 hover:text-blue-800">Home</router-link>
          </li>
          <li>
            <span>/</span>
          </li>
          <li class="text-gray-500" aria-current="page">Generate Report</li>
        </ol>
      </nav>
  
      <!-- Horizontal Bar with Dropdowns -->
      <div class="filter-bar">
        <div class="form-group">
          <label for="subscriberStatus">Subscribers</label>
          <select id="subscriberStatus" v-model="form.subscriberStatus">
            <option value="" disabled>Select Status</option>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>
        </div>
  
        <div class="form-group">
          <label for="userType">User Type</label>
          <select id="userType" v-model="form.userType">
            <option value="" disabled>Select User Type</option>
            <option value="admin">Admin</option>
            <option value="editor">Editor</option>
            <option value="regular">Regular</option>
          </select>
        </div>
      </div>
  
      <button class="btn generate-btn" @click="generateReport">Generate</button>
  
      <!-- Report Display Section -->
      <div v-if="reportGenerated" class="report-section">
        <h2 class="report-title">Report</h2>
        <div v-if="reportData.length === 0" class="no-data">No data to display.</div>
        <div v-for="(item, index) in reportData" :key="index" class="report-card">
          <p><strong>Name:</strong> {{ item.name }}</p>
          <p><strong>Status:</strong> {{ item.status }}</p>
          <p><strong>User Type:</strong> {{ item.userType }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import magazineSubscriberService from '../services/magazineSubscriberService';
  
  export default {
    data() {
      return {
        form: {
          subscriberStatus: '',
          userType: ''
        },
        reportGenerated: false,
        reportData: []
      };
    },
    methods: {
      async generateReport() {
        try {
          const response = await magazineSubscriberService.getFilteredSubscribers(this.form.subscriberStatus, this.form.userType);
          this.reportData = response.data;
          this.reportGenerated = true;
        } catch (error) {
          console.error("Error fetching report data:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #f9fafb; /* Light gray background for readability */
    border-radius: 8px;
    padding: 2rem;
    margin-top: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  }
  
  .title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1.5rem;
    color: #1f2937;
  }
  
  .home-link {
    display: inline-block;
    margin-bottom: 1rem;
    color: #3b82f6;
    text-decoration: underline;
  }
  
  .filter-bar {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    align-items: center;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    min-width: 200px;
  }
  
  label {
    margin-bottom: 0.5rem;
    font-weight: 600;
  }
  
  select {
    padding: 0.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 4px;
    transition: border-color 0.3s;
  }
  
  select:focus {
    border-color: #3b82f6;
    outline: none;
  }
  
  .btn {
    padding: 0.75rem 1.5rem;
    background-color: #3b82f6;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .btn:hover {
    background-color: #2563eb;
  }
  
  .report-section {
    margin-top: 2rem;
  }
  
  .report-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }
  
  .no-data {
    color: #6b7280;
    font-style: italic;
    text-align: center;
  }
  
  .report-card {
    padding: 1.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    margin-bottom: 1rem;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  
  .report-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }
  
  .report-card p {
    margin: 0.5rem 0;
    color: #4b5563;
  }
  </style>
  