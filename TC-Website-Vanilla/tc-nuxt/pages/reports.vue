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

    <!-- Filter Section -->
    <div class="filter-bar">
      <div class="form-group">
        <label for="subscriberType">Subscriber Type</label>
        <select id="subscriberType" v-model="form.subscriberType">
          <option value="" disabled>Select</option>
          <option v-for="type in subscriberTypes" :key="type._id" :value="type.name">
            {{ type.name }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="subscriberCategory">Subscriber Category</label>
        <select id="subscriberCategory" v-model="form.subscriberCategory">
          <option value="" disabled>Select</option>
          <option v-for="category in subscriberCategories" :key="category._id" :value="category.name">
            {{ category.name }}
          </option>
        </select>
      </div>
    
      <div class="form-group">
        <label for="subscriberStatus" class="switch-label">Subscriber Status</label>
        <div class="switch-container">
          <span :class="form.subscriberStatus === 'active' ? 'text-green-600 font-bold' : 'text-gray-400'">Active</span>
          <label class="switch">
            <input type="checkbox" v-model="isActive" @change="toggleSubscriberStatus" />
            <span class="slider round"></span>
          </label>
          <span :class="form.subscriberStatus === 'inactive' ? 'text-red-600 font-bold' : 'text-gray-400'">Inactive</span>
        </div>
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
            <p>{{ item.Name }}</p>
            <p>{{ item['Address line 1'] }}</p>
            <p>{{ item['Address line 2'] }}</p>
            <p>{{ item.City }}</p>
            <p>{{ item.District }}</p>
            <p>{{ item.State }}</p>
            <p>{{ item.Pincode }}</p>
            <p>{{ item['Phone Number'] }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import reportService from '../services/reportService';
import subscriberTypeService from '../services/subscriberTypeService';
import subscriberCategoryService from '../services/subscriberCategoryService';

export default {
  data() {
    return {
      form: {
        subscriberStatus: 'active', // Default to active
        subscriberType: '',
        subscriberCategory: '',
      },
      isActive: true, // Switch state for active/inactive subscribers
      reportGenerated: false,
      reportData: [],
      subscriberTypes: [],
      subscriberCategories: [],
    };
  },
  methods: {
    toggleSubscriberStatus() {
      this.form.subscriberStatus = this.isActive ? 'active' : 'inactive';
    },
    fetchSubscriberTypes() {
      subscriberTypeService.getSubscriberTypes()
        .then(response => {
          this.subscriberTypes = response.data;
        })
        .catch(error => {
          console.error('Error fetching subscriber types:', error);
          alert('Failed to fetch subscriber types. Please try again.');
        });
    },
    fetchSubscriberCategories() {
      subscriberCategoryService.getSubscriberCategories()
        .then(response => {
          this.subscriberCategories = response.data;
        })
        .catch(error => {
          console.error('Error fetching subscriber categories:', error);
          alert('Failed to fetch subscriber categories. Please try again.');
        });
    },
    generateReport() {
      const filters = {
        status: this.form.subscriberStatus,
        subscriberType: this.form.subscriberType,
        subscriberCategory: this.form.subscriberCategory,
      };

      reportService.getReport(filters)
        .then(response => {
          if (response.data.length > 0) {
            this.reportData = response.data;
            this.reportGenerated = true;
          } else {
            this.reportData = [];
            this.reportGenerated = false;
          }
        })
        .catch(error => {
          console.error('There was an error fetching the report!', error);
          this.reportData = [];
          this.reportGenerated = false;
          alert('Failed to fetch the report. Please try again.');
        });
    },
    downloadPdf() {
      const filters = {
        status: this.form.subscriberStatus,
        subscriberType: this.form.subscriberType,
        subscriberCategory: this.form.subscriberCategory,
      };

      reportService.downloadPdfReport(filters)
        .then((response) => {
        // Get the current datetime
        const now = new Date();
        const formattedDate = now.toISOString().slice(0, 10); // YYYY-MM-DD
        const formattedTime = now.toISOString().slice(11, 19).replace(/:/g, '-'); // HH-MM-SS

        // Set the filename with IST timezone
        const filename = `subscriber_report_${formattedDate}_${formattedTime}_IST.pdf`;

        // Handle the PDF download
        const url = window.URL.createObjectURL(new Blob([response.data], { type: 'application/pdf' }));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      })
      .catch((error) => {
        console.error('Error downloading the PDF:', error);
        alert('Failed to download the PDF. Please try again.');
      });
    },
  },
  created() {
    this.fetchSubscriberTypes();
    this.fetchSubscriberCategories();
  },
};
</script>

<style scoped>
/* Updated Styles for Switch */
.switch-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: 0.4s;
  border-radius: 24px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 4px;
  bottom: 3px;
  background-color: white;
  transition: 0.4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #4caf50;
}

input:checked + .slider:before {
  transform: translateX(26px);
}

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
