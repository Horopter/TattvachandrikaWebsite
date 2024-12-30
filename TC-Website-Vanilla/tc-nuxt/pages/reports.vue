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
      generateReport() {
        // Simulate report generation logic
        this.reportData = [
          { name: 'John Doe', status: this.form.subscriberStatus, userType: this.form.userType },
          { name: 'Jane Smith', status: this.form.subscriberStatus, userType: this.form.userType }
        ];
  
        this.reportGenerated = true; // Show the report section
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #ffedcc; /* Dim orange background */
    border-radius: 8px;
    padding: 2rem;
    margin-top: 1rem;
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
    align-items: center; /* Center align items */
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 0.5rem;
    font-weight: 600;
  }
  
  select {
    padding: 0.5rem; /* Increased padding for better usability */
    border: 1px solid #ccc;
    border-radius: 4px;
    transition: border-color 0.3s; /* Smooth transition on focus */
  }
  
  select:focus {
    border-color: #3b82f6; /* Highlight border on focus */
    outline: none; /* Remove default outline */
  }
  
  .btn {
    padding: 0.5rem 1rem; /* Adjusted padding */
    background-color: #3b82f6; /* Button color */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s; /* Smooth transition on hover */
  }
  
  .btn:hover {
    background-color: #2563eb; /* Darker shade on hover */
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
    color: #6b7280; /* Gray color for no data message */
    font-style: italic; /* Italic style for emphasis */
  }
  
  .report-card {
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 1rem;
    background-color: #ffffff; /* White background for report cards */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    transition: transform 0.2s; /* Smooth transition on hover */
  }
  
  .report-card:hover {
    transform: translateY(-3px); /* Lift effect on hover */
  }
  </style>
  