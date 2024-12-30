<template>
    <div class="container mx-auto p-6">
      <h1 class="title">Add New User</h1>
      <form @submit.prevent="handleSubmit" class="form">
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input type="text" id="firstName" v-model="form.firstName" required />
        </div>
        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input type="text" id="lastName" v-model="form.lastName" required />
        </div>
        <div class="form-group">
          <label for="address">Address</label>
          <input type="text" id="address" v-model="form.address" required />
        </div>
        <div class="form-group">
          <label for="phone">Phone No</label>
          <input type="tel" id="phone" v-model="form.phone" required />
        </div>
        <div class="form-group">
          <label for="subscription">Subscription Details</label>
          <select id="subscription" v-model="form.subscription" required>
            <option value="" disabled>Select Subscription</option>
            <option value="2_years">2 Years</option>
            <option value="5_years">5 Years</option>
            <option value="10_years">10 Years</option>
          </select>
        </div>
        <div class="form-group">
          <label for="userType">Type of User</label>
          <select id="userType" v-model="form.userType" required>
            <option value="" disabled>Select User Type</option>
            <option value="subscriber">Subscriber</option>
            <option value="admin">Admin</option>
            <option value="editor">Editor</option>
          </select>
        </div>
        <div class="buttons">
          <button type="submit" class="btn submit">Submit</button>
          <button type="button" @click="resetForm" class="btn reset">Reset</button>
          <nuxt-link to="/HomePage" class="btn cancel">Cancel</nuxt-link>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AddNewUser',
    data() {
      return {
        form: {
          firstName: '',
          lastName: '',
          address: '',
          phone: '',
          subscription: '',
          userType: ''
        }
      };
    },
    methods: {
      handleSubmit() {
        // Handle form submission logic here
        console.log('Form submitted:', this.form);
        // You can reset the form or redirect after submission
        this.resetForm();
      },
      resetForm() {
        this.form = {
          firstName: '',
          lastName: '',
          address: '',
          phone: '',
          subscription: '',
          userType: ''
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #ffedcc; /* Dim orange background */
    border-radius: 8px; /* Rounded corners */
    padding: 2rem; /* Extra padding for the container */
    margin-top: 1rem;
  }
  
  .title {
    font-size: 2rem; /* Title size */
    font-weight: bold;
    margin-bottom: 1.5rem;
    color: #1f2937; /* Darker text color */
  }
  
  .form {
    display: grid;
    gap: 1.5rem; /* Space between form elements */
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
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
  
  .buttons {
    display: flex;
    gap: 1rem; /* Space between buttons */
  }
  
  .btn {
    padding: 0.75rem 1.5rem; /* Padding for buttons */
    border: none; /* Remove border */
    border-radius: 4px; /* Rounded corners */
    color: white; /* Text color */
    cursor: pointer; /* Pointer cursor on hover */
  }
  
  .submit {
    background-color: #3b82f6; /* Submit button color */
  }
  
  .reset {
    background-color: #f59e0b; /* Reset button color */
  }
  
  .cancel {
    background-color: #ef4444; /* Cancel button color */
  }
  </style>
  