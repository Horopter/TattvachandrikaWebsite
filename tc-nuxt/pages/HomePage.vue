<template>
  <div class="container mx-auto p-6">
    <h1 class="title">Welcome to Tattvachandrika Admin Portal</h1>
    <nav aria-label="breadcrumb" class="breadcrumb">
      <ol class="flex space-x-2 text-sm text-gray-700">
        <li class="text-gray-500"><nuxt-link to="/">Home</nuxt-link></li>
      </ol>
    </nav>
    <ul class="link-list">
      <li class="link-item">
        <nuxt-link to="/subscriptionModes" class="link">Manage Subscription Modes</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/subscriptionLanguages" class="link">Manage Subscription Languages</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/subscriberCategories" class="link">Manage Subscriber Categories</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/subscriberTypes" class="link">Manage Subscriber Types</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/subscriptionPlans" class="link">Manage Subscription Plans</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/paymentModes" class="link">Manage Payment Modes</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/MagazineSubscribers" class="link">Manage Subscribers</nuxt-link>
      </li>
      <li class="link-item">
        <nuxt-link to="/reports" class="link">Manage Reports</nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
.container {
  background-color: #ffedcc; /* Dim orange background */
  border-radius: 8px; /* Rounded corners */
  padding: 2rem; /* Extra padding for the container */
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

.link-list {
  list-style: none; /* Remove default list style */
  padding: 0; /* Remove padding */
}

.link-item {
  background-color: white; /* White background for each item */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  transition: transform 0.2s, box-shadow 0.2s; /* Smooth transition */
  margin-bottom: 1.5rem; /* Margin between cards */
}

.link-item:hover {
  transform: translateY(-3px); /* Lift effect on hover */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover */
}

.link {
  display: block; /* Make link fill the entire item */
  padding: 1rem; /* Add padding */
  color: #3b82f6; /* Blue color for links */
  text-decoration: none; /* Remove underline */
  font-weight: 500; /* Medium font weight */
}

.link:hover {
  text-decoration: underline; /* Underline on hover */
}
</style>
