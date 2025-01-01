<template>
    <div class="container mx-auto p-6">
      <h1 class="title">View/Update User Details</h1>
  
      <div v-if="!userFetched">
        <form @submit.prevent="fetchUserDetails" class="search-form">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" v-model="searchParams.name" required />
          </div>
          <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" v-model="searchParams.phone" required />
          </div>
          <button class="btn fetch-btn">Fetch User Details</button>
          <button class="btn update-btn"><nuxt-link to="/HomePage">Go Back</nuxt-link></button>
        </form>
      </div>
  
      <div v-if="userFetched" class="user-form">
        <h2 class="form-title">User Details</h2>
        <form @submit.prevent="updateUserDetails">
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" v-model="user.firstName" required />
          </div>
          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" v-model="user.lastName" required />
          </div>
          <div class="form-group">
            <label for="address">Address</label>
            <input type="text" id="address" v-model="user.address" required />
          </div>
          <div class="form-group">
            <label for="subscription">Subscription Details</label>
            <select id="subscription" v-model="user.subscription" required>
              <option value="2_years">2 Years</option>
              <option value="5_years">5 Years</option>
              <option value="10_years">10 Years</option>
            </select>
          </div>
          <button class="btn update-btn">Update User Details</button>
          <button class="btn update-btn"><nuxt-link to="/HomePage">Go Back</nuxt-link></button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchParams: {
          name: '',
          phone: ''
        },
        user: {
          firstName: '',
          lastName: '',
          address: '',
          phone: '',
          subscription: ''
        },
        userFetched: false
      };
    },
    methods: {
      fetchUserDetails() {
        // Simulated API call to fetch user details based on name and phone
        const mockUserData = {
          firstName: 'John',
          lastName: 'Doe',
          address: '123 Main St',
          phone: this.searchParams.phone,
          subscription: '5_years'
        };
  
        // Check if the provided details match (in a real app, you would check against a database)
        if (this.searchParams.name === 'John' && this.searchParams.phone === '1234567890') {
          this.user = mockUserData;
          this.userFetched = true; // User details fetched successfully
        } else {
          alert('User not found. Please check the details and try again.');
        }
      },
      updateUserDetails() {
        // Simulate updating user details (you would normally send this to an API)
        console.log('Updated user details:', this.user);
        alert('User details updated successfully!');
        this.resetForm();
      },
      resetForm() {
        this.searchParams = { name: '', phone: '' };
        this.user = { firstName: '', lastName: '', address: '', phone: '', subscription: '' };
        this.userFetched = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    margin-top: 2rem;
    background-color: #ffedcc; /* Dim orange background */
    border-radius: 8px; /* Rounded corners */
    padding: 2rem; /* Extra padding for the container */
  }
  
  .title {
    font-size: 2rem; /* Title size */
    font-weight: bold;
    margin-bottom: 1.5rem;
    color: #1f2937; /* Darker text color */
  }
  
  .search-form, .user-form {
    margin-bottom: 2rem; /* Space between forms */
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem; /* Space between form fields */
  }
  
  label {
    margin-bottom: 0.5rem; /* Space between label and input */
    font-weight: 600; /* Bold labels */
  }
  
  input, select {
    padding: 0.5rem; /* Padding for inputs */
    border: 1px solid #ccc; /* Border color */
    border-radius: 4px; /* Rounded corners */
  }
  
  .btn {
    padding: 0.5rem 1rem; /* Button padding */
    background-color: #3b82f6; /* Button color */
    color: white; /* Button text color */
    border: none; /* Remove border */
    border-radius: 4px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor */
    margin-right: 10px;
  }
  
  .btn:hover {
    background-color: #2563eb; /* Darker shade on hover */
  }
  
  .form-title {
    font-size: 1.5rem; /* Title size for user details */
    margin-bottom: 1rem; /* Space below title */
  }
  </style>
  