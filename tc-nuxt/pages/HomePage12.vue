<template>
    <div class="container mx-auto p-6">
      <h1 class="title">Admin Dashboard</h1>
      <nav aria-label="breadcrumb" class="breadcrumb">
        <ol class="flex space-x-2 text-sm text-gray-700">
          <li class="text-gray-500">Home</li>
        </ol>
      </nav>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="card bg-blue-600">
          <nuxt-link to="/addUser" class="card-link">Add New User</nuxt-link>
        </div>
        <div class="card bg-teal-600">
          <nuxt-link to="/updateUser" class="card-link">View/Update User Details</nuxt-link>
        </div>
        <div class="card bg-amber-600">
          <nuxt-link to="/updateSubscriber" class="card-link">View/Update Subscription Details</nuxt-link>
        </div>
        <div class="card bg-indigo-600">
          <nuxt-link to="/reports" class="card-link">Reports</nuxt-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DashboardPage'
  };
  </script>
  
  <style scoped>
  .container {
    background-color: #ffedcc; /* Light gray background */
    border-radius: 8px; /* Rounded corners */
    padding: 2rem; /* Extra padding for the container */
    margin-top: 60px;
  }
  
  .title {
    font-size: 2.5rem; /* Larger font size */
    font-weight: bold;
    margin-bottom: 1.5rem;
    color: #1f2937; /* Darker text color */
  }
  
  .breadcrumb {
    margin-bottom: 1rem;
    color: #6b7280; /* Gray text color */
  }
  
  .grid {
    display: grid; /* Use CSS grid */
    gap: 1.5rem; /* Gap between grid items */
  }
  
  .card {
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    transition: transform 0.2s, box-shadow 0.2s; /* Smooth transition */
    color: white; /* Text color for the cards */
    text-align: center; /* Center text */
    padding: 2rem; /* Add padding */
    font-family: 'Arial', sans-serif; /* Use a formal font */
  }
  
  .card:hover {
    transform: translateY(-2px); /* Slight lift effect on hover */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* Enhanced shadow on hover */
  }
  
  .card-link {
    color: white; /* White text color for links */
    text-decoration: none; /* Remove underline */
    font-weight: 500; /* Medium font weight */
    font-size: 1.1rem; /* Slightly larger font size */
  }
  
  .card-link:hover {
    text-decoration: underline; /* Underline on hover */
  }
  
  /* Additional colors for cards */
  .bg-blue-600 { background-color: #2563eb; } /* Blue */
  .bg-teal-600 { background-color: #0d9488; } /* Teal */
  .bg-amber-600 { background-color: #ca8a04; } /* Amber */
  .bg-indigo-600 { background-color: #4338ca; } /* Indigo */
  </style>
  