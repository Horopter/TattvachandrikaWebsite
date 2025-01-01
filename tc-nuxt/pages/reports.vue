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

    <div class="button-group">
      <button class="btn generate-btn" @click="generateReport">Generate</button>
      <button class="btn download-btn" @click="downloadPdf">Download PDF</button>
    </div>

    <!-- Report Display Section -->
    <div v-if="reportGenerated" class="report-section">
      <h2 class="report-title">Report</h2>
      <div v-if="reportData.length === 0" class="no-data">No data to display.</div>
      <div class="card-container">
        <div v-for="(item, index) in reportData" :key="index" class="report-card">
          <div class="card-content">
            <p><strong>Name:</strong> {{ item.Name }}</p>
            <p><strong>Address Line 1:</strong> {{ item['Address line 1'] }}</p>
            <p><strong>Address Line 2:</strong> {{ item['Address line 2'] || 'N/A' }}</p>
            <p><strong>City:</strong> {{ item.City }}</p>
            <p><strong>District:</strong> {{ item.District || 'N/A' }}</p>
            <p><strong>State:</strong> {{ item.State }}</p>
            <p><strong>Pincode:</strong> {{ item.Pincode }}</p>
            <p><strong>Phone Number:</strong> {{ item['Phone Number'] }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

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
        const response = await axios.get('http://127.0.0.1:8000/api/subscribers/report/', {
          headers: {
            'accept': 'application/json',
            'X-CSRFToken': 'gvzuJHZXUWbz1Gw6AIEOMe3KkOcM64f2upiBzg390GsdYB5cAIRjpyfMDFoceBnE'
          },
          params: {
            status: this.form.subscriberStatus,
            userType: this.form.userType
          }
        });

        this.reportData = response.data;
        this.reportGenerated = true;
      } catch (error) {
        console.error('Error fetching the report:', error);
        alert('Failed to fetch the report. Please try again.');
      }
    },
    async downloadPdf() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/subscribers/generate_pdf_report/', {
          headers: {
            'accept': 'application/json',
            'X-CSRFToken': 'gvzuJHZXUWbz1Gw6AIEOMe3KkOcM64f2upiBzg390GsdYB5cAIRjpyfMDFoceBnE'
          },
          responseType: 'blob'
        });

        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'subscriber_report.pdf');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      } catch (error) {
        console.error('Error downloading the PDF:', error);
        alert('Failed to download the PDF. Please try again.');
      }
    }
  }
};
</script>

<style scoped>
.container {
  background-color: #ffedcc;
  border-radius: 8px;
  padding: 2rem;
  margin-top: 1rem;
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
}

label {
  margin-bottom: 0.5rem;
  font-weight: 600;
}

select {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  transition: border-color 0.3s;
}

select:focus {
  border-color: #3b82f6;
  outline: none;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.generate-btn {
  padding: 0.5rem 1rem;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.generate-btn:hover {
  background-color: #2563eb;
}

.download-btn {
  padding: 0.5rem 1rem;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.download-btn:hover {
  background-color: #059669;
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
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.report-card {
  flex: 1 1 calc(50% - 1rem);
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.report-card:hover {
  transform: translateY(-3px);
}
</style>
